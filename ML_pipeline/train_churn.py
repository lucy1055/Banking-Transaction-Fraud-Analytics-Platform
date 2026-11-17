import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

print("Generating customer churn dataset...")

# 1. Generate Synthetic Dataset
np.random.seed(42)
n_samples = 5000

account_age_months = np.randint(1, 72, size=n_samples) if hasattr(np, 'randint') else np.random.randint(1, 72, size=n_samples)
monthly_transactions = np.random.poisson(lam=10, size=n_samples)
avg_balance = np.exponential(scale=5000, size=n_samples) if hasattr(np, 'exponential') else np.random.exponential(scale=5000, size=n_samples)
support_tickets = np.random.poisson(lam=1, size=n_samples)

# Rule for churn generation
churn_labels = []
for i in range(n_samples):
    risk = 0.1
    if support_tickets[i] > 3:
        risk += 0.4
    if monthly_transactions[i] < 4:
        risk += 0.3
    if avg_balance[i] < 500:
        risk += 0.2
        
    is_c = 1 if np.random.rand() < risk else 0
    churn_labels.append(is_c)

df = pd.DataFrame({
    'account_age_months': account_age_months,
    'monthly_transactions': monthly_transactions,
    'avg_balance': avg_balance,
    'support_tickets': support_tickets,
    'is_churned': churn_labels
})

# 2. Train-Test Split
X = df[['account_age_months', 'monthly_transactions', 'avg_balance', 'support_tickets']]
y = df['is_churned']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Training
print("Training Gradient Boosting Classifier for Churn Prediction...")
model = GradientBoostingClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluation
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# 5. Save the Model
joblib.dump(model, 'churn_model.pkl')
print("Churn prediction model successfully saved as 'churn_model.pkl'!")