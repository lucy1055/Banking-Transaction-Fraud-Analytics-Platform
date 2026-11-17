import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

print("Generating synthetic transaction dataset for fraud detection...")

# 1. Generate Synthetic Dataset
np.random.seed(42)
n_samples = 5000

amounts = np.random.exponential(scale=200, size=n_samples)
transaction_hours = np.random.randint(0, 24, size=n_samples)
is_foreign = np.random.choice([0, 1], size=n_samples, p=[0.9, 0.1])
velocity = np.random.poisson(lam=2, size=n_samples)

# Rule for fraud generation
fraud_labels = []
for i in range(n_samples):
    risk = 0.05
    if amounts[i] > 1000:
        risk += 0.4
    if is_foreign[i] == 1:
        risk += 0.3
    if velocity[i] > 5:
        risk += 0.2
    
    is_f = 1 if np.random.rand() < risk else 0
    fraud_labels.append(is_f)

df = pd.DataFrame({
    'amount': amounts,
    'transaction_hour': transaction_hours,
    'is_foreign': is_foreign,
    'velocity': velocity,
    'is_fraud': fraud_labels
})

# 2. Train-Test Split
X = df[['amount', 'transaction_hour', 'is_foreign', 'velocity']]
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Training
print("Training Random Forest Classifier for Fraud Detection...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluation
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# 5. Save the Model
joblib.dump(model, 'fraud_model.pkl')
print("Fraud detection model successfully saved as 'fraud_model.pkl'!")