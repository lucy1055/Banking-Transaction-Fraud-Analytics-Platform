-- 1. Users / Customers Table
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bank Accounts Table (3NF Normalized)
CREATE TABLE IF NOT EXISTS accounts (
    account_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    account_type VARCHAR(20) CHECK (account_type IN ('Savings', 'Current')),
    balance NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Transactions Table (ACID Compliant Log)
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    sender_account_id INT REFERENCES accounts(account_id),
    receiver_account_id INT REFERENCES accounts(account_id),
    amount NUMERIC(12, 2) NOT NULL CHECK (amount > 0),
    transaction_status VARCHAR(20) DEFAULT 'SUCCESS', 
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Fraud Logs Table
CREATE TABLE IF NOT EXISTS fraud_logs (
    fraud_log_id SERIAL PRIMARY KEY,
    transaction_id INT REFERENCES transactions(transaction_id) ON DELETE CASCADE,
    risk_score FLOAT NOT NULL,
    is_fraudulent BOOLEAN DEFAULT FALSE,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for Fast Lookups & Analytics
CREATE INDEX idx_transactions_sender ON transactions(sender_account_id);
CREATE INDEX idx_transactions_timestamp ON transactions(timestamp);
CREATE INDEX idx_accounts_user ON accounts(user_id);