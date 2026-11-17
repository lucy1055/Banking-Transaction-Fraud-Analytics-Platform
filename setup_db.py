import psycopg2

try:
    # 1. Connect to default postgres database to create banking_db
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Aadi@1512", host="localhost", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'banking_db'")
    if not cursor.fetchone():
        cursor.execute("CREATE DATABASE banking_db;")
        print("Database 'banking_db' created successfully!")
    else:
        print("Database 'banking_db' already exists!")

    cursor.close()
    conn.close()

    # 2. Connect to banking_db and create tables directly
    conn2 = psycopg2.connect(dbname="banking_db", user="postgres", password="Aadi@1512", host="localhost", port="5432")
    cursor2 = conn2.cursor()

    schema_sql = """
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS accounts (
        account_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
        balance NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
        account_type VARCHAR(20) DEFAULT 'Savings',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id SERIAL PRIMARY KEY,
        sender_account_id INT REFERENCES accounts(account_id),
        receiver_account_id INT REFERENCES accounts(account_id),
        amount NUMERIC(12, 2) NOT NULL,
        is_fraud BOOLEAN DEFAULT FALSE,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS fraud_logs (
        log_id SERIAL PRIMARY KEY,
        transaction_id INT REFERENCES transactions(transaction_id),
        reason TEXT,
        flagged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor2.execute(schema_sql)
    conn2.commit()
    print("All tables (users, accounts, transactions, fraud_logs) created successfully!")

    cursor2.close()
    conn2.close()

except Exception as e:
    print(f"Error occurred: {e}")
