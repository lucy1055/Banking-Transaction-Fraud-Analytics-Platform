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

    # 2. Connect to banking_db and create tables from schema.sql
    conn2 = psycopg2.connect(dbname="banking_db", user="postgres", password="Aadi@1512", host="localhost", port="5432")
    cursor2 = conn2.cursor()

    with open("sql/schema.sql", "r") as f:
        schema_sql = f.read()

    cursor2.execute(schema_sql)
    conn2.commit()
    print("All tables (users, accounts, transactions, fraud_logs) created successfully!")

    cursor2.close()
    conn2.close()

except Exception as e:
    print(f"Error occurred: {e}")
