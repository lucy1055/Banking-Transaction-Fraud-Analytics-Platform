# Banking Transaction & Fraud Analytics Platform

An end-to-end banking transaction engine featuring ACID-compliant transfer logic, a normalized 3NF PostgreSQL database, real-time machine learning fraud detection, churn prediction models, a FastAPI backend, and an interactive Streamlit dashboard.

---

## 🚀 Key Features

- **ACID-Compliant Transactions:** Built with row-level locking and strict relational constraints in PostgreSQL to ensure secure, concurrent bank transfers without race conditions.
- **Fraud & Churn Analytics:** Integrated machine learning pipelines that evaluate transactions in real-time to flag anomalies, assess fraud risks, and predict customer churn.
- **FastAPI Backend:** High-performance asynchronous REST API endpoints powering transaction processing, user management, and analytics data retrieval.
- **Interactive Streamlit Dashboard:** A user-friendly frontend allowing users and administrators to view live transaction feeds, fraud alerts, and analytics charts.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python, Uvicorn
- **Database:** PostgreSQL (3NF Normalized Schema, SQL)
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend / Dashboard:** Streamlit
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
banking-fraud-analytics/
│
├── backend/                  # FastAPI application & business logic
│   ├── main.py               # API entry point & routes
│   ├── database.py           # DB connection & session management
│   ├── models.py             # SQLAlchemy ORM models
│   └── crud.py               # Database CRUD operations
│
├── frontend/                 # Interactive user interface
│   └── app.py                # Streamlit dashboard application
│
├── ml_pipeline/              # Machine learning models & training scripts
│   ├── train_fraud.py        # Fraud detection model training
│   ├── train_churn.py        # Customer churn prediction training
│   └── model.pkl             # Serialized trained ML models
│
├── sql/                      # Database schemas and analytical queries
│   ├── schema.sql            # 3NF Database creation scripts
│   └── analytics_queries.sql # Complex SQL queries for reporting
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
