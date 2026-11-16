# Banking Transaction & Fraud Analytics Platform

An end-to-end banking transaction engine featuring ACID-compliant transfer logic, a normalized 3NF PostgreSQL database, real-time machine learning fraud detection, churn prediction models, a FastAPI backend, and an interactive Streamlit dashboard.

---

## Key Features

- **ACID-Compliant Transactions:** Built with row-level locking and strict relational constraints in PostgreSQL to ensure secure, concurrent bank transfers without race conditions.
- **Fraud & Churn Analytics:** Integrated machine learning pipelines that evaluate transactions in real-time to flag anomalies, assess fraud risks, and predict customer churn.
- **FastAPI Backend:** High-performance asynchronous REST API endpoints powering transaction processing, user management, and analytics data retrieval.
- **Interactive Streamlit Dashboard:** A user-friendly frontend allowing users and administrators to view live transaction feeds, fraud alerts, and analytics charts.

---

## Tech Stack

- **Backend:** FastAPI, Python, Uvicorn
- **Database:** PostgreSQL (3NF Normalized Schema, SQL)
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend / Dashboard:** Streamlit
- **Version Control:** Git & GitHub

---

## Project Structure

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
```
## WHY I BUILT THIS PROJECT
I understand database normalization (3NF), ACID properties, and machine learning classification models theoretically through standard academic assignments and isolated datasets. However, I wanted to experience how a production-grade financial backend handles high-concurrency fund transfers, strict transaction isolation, and real-time fraud scoring without compromising data integrity.

I built an end to end `Banking Transaction & Fraud Analytics Platform` that models real-world banking operations under concurrent stress.
My goal is to observe and solve critical financial engineering challenges:
* **Concurrency & Race Conditions:** How multiple simultaneous fund transfers affect account balances and how row-level locking prevents double-spending.
* **Real time fraud and customer inferance:** How incoming high-frequency transaction streams can be evaluated instantaneously by machine learning models without introducing latency bottlenecks in the API layer.
* **Database Architecture Trade-offs:** How Third Normal Form schema constraints, foreign key indexing, and optimized analytical queries balance write performance with complex reporting needs.
* 
## The core Architecture of this Platform
The platform models a secure, multitier banking engine. Every incoming transaction request flows through an integrated pipeline:
* **API Ingestion:** Asynchronous FastAPI endpoints receive transaction payloads, validating user credentials and account states.
* **ACID-Compliant Transaction Execution:** The backend initiates a database session with strict isolation levels, utilizing row-level locks (SELECT ... FOR UPDATE) to safely debit and credit balances.
* **Real-Time Fraud Evaluation:** Completed transactions trigger an evaluation hook where serialized machine learning models analyze transaction velocity, amount anomalies, and geographical patterns.
* **State Persistence & Auditing:** Updated ledger entries, account balances, and fraud logs are atomically committed to a normalized PostgreSQL database.
* **Analytical Telemetry & Dashboard:** The Streamlit dashboard queries aggregated SQL views to present live transaction feeds, fraud alert metrics, and customer churn predictions.

## Design Rationale & Concurrency Control
* **Row-Level Locking:** To prevent race conditions where two concurrent requests try to withdraw from the same account simultaneously, the execution engine serializes critical balance updates using database-level locking primitives.
* **Normalized 3NF Schema:** Ensures zero data redundancy across user accounts, transaction logs, and branch records, minimizing anomalies during multi-table joins.
* **Decoupled Analytics:** Machine learning inference is structured to run efficiently alongside the core transactional loop, ensuring that analytical processing never blocks critical financial operations.
* 
## System & Analytical Metrics
* **Database & API Performance:** Transaction Throughput (TPS), API Response Latency, and Concurrency Success Rate.
* **ML Model Performance:** Precision, Recall, False Positive Rate, and Inference Execution Time.
* **Financial Integrity Metrics:** Zero-sum balance verification across accounts and 100% ACID compliance compliance validation.

## Build and Run
Clone and Setup Environment:
``` text
git clone https://github.com/lucy1055/Banking-Transaction-Fraud-Analytics-Platform.git
cd banking-fraud-analytics
pip install -r requirements.txt
```
## Initialize Database Schema:
```text
psql -U postgres -d banking_db -f sql/schema.sql
```
## Run the FastAPI Backend:
```text
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
## Launch the Streamlit Analytics Dashboard:
```text
cd frontend
streamlit run app.py
```
## Project Goal
The purpose of this project is to build deep practical intuition about backend engineering, financial data security, and the integration of machine learning into high-stakes, concurrent transaction systems.
