import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Banking & Fraud Analytics Dashboard",
    page_icon="🏦",
    layout="wide"
)

# API Base URL (FastAPI backend)
API_URL = "http://127.0.0.1:8000"

st.title("🏦 Banking Transaction & Fraud Analytics Platform")
st.markdown("Monitor real-time ACID fund transfers, evaluate fraud risks, and analyze customer behavior.")

# Sidebar Navigation
st.sidebar.header("Navigation Menu")
choice = st.sidebar.selectbox("Choose Action", ["Dashboard Home", "Create User & Account", "Make Transfer", "Fraud & Churn Analytics"])

if choice == "Dashboard Home":
    st.subheader("📊 System Overview")
    st.write("Welcome to the platform dashboard. Use the sidebar to navigate through user creation, secure fund transfers, and ML analytics.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="System Status", value="Online 🟢")
    col2.metric(label="ACID Compliance", value="Active (Row Locks)")
    col3.metric(label="ML Models", value="Trained & Ready")

elif choice == "Create User & Account":
    st.subheader("👤 Register User & Open Bank Account")
    
    with st.form("user_form"):
        st.markdown("### Step 1: User Details")
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        
        submitted_user = st.form_submit_button("Create User")
        if submitted_user:
            res = requests.post(f"{API_URL}/users/", json={"full_name": full_name, "email": email, "phone_number": phone})
            if res.status_code == 200:
                user_data = res.json()
                st.success(f"User created successfully! User ID: {user_data['user_id']}")
            else:
                st.error(f"Error: {res.text}")

    with st.form("account_form"):
        st.markdown("### Step 2: Bank Account Details")
        user_id = st.number_input("User ID", min_value=1, step=1)
        account_type = st.selectbox("Account Type", ["Savings", "Current"])
        initial_balance = st.number_input("Initial Deposit Amount (₹)", min_value=0.0, value=1000.0)
        
        submitted_acc = st.form_submit_button("Open Account")
        if submitted_acc:
            res = requests.post(f"{API_URL}/accounts/", json={"user_id": user_id, "account_type": account_type, "initial_balance": initial_balance})
            if res.status_code == 200:
                acc_data = res.json()
                st.success(f"Account opened successfully! Account ID: {acc_data['account_id']}")
            else:
                st.error(f"Error: {res.text}")

elif choice == "Make Transfer":
    st.subheader("💸 Secure Fund Transfer (ACID Compliant)")
    
    with st.form("transfer_form"):
        sender_id = st.number_input("Sender Account ID", min_value=1, step=1)
        receiver_id = st.number_input("Receiver Account ID", min_value=1, step=1)
        amount = st.number_input("Transfer Amount (₹)", min_value=1.0, value=500.0)
        
        submitted_transfer = st.form_submit_button("Execute Transfer")
        if submitted_transfer:
            res = requests.post(f"{API_URL}/transfer/", json={"sender_id": sender_id, "receiver_id": receiver_id, "amount": amount})
            if res.status_code == 200:
                data = res.json()
                st.success(f"Transaction Successful! Transaction ID: {data.get('transaction_id')}")
            else:
                st.error(f"Transfer Failed: {res.json().get('detail')}")

elif choice == "Fraud & Churn Analytics":
    st.subheader("🛡️ Machine Learning Fraud & Churn Insights")
    st.info("Simulated real-time scoring based on transaction velocity, amount anomaly, and customer activity patterns.")
    
    # Mock Analytics View
    chart_data = pd.DataFrame({
        'Transaction Risk Score': [0.12, 0.88, 0.05, 0.94, 0.22, 0.65],
        'Status': ['Safe', 'Fraud Alert', 'Safe', 'Fraud Alert', 'Safe', 'Review']
    })
    st.bar_chart(chart_data['Transaction Risk Score'])
    st.write("Recent transaction anomaly evaluations processed by the Random Forest engine.")