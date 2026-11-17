from sqlalchemy import Column, Integer, String, Numeric, Boolean, TIMESTAMP, ForeignKey, Float
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone_number = Column(String(15))
    created_at = Column(TIMESTAMP, server_default=func.now())

class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    account_type = Column(String(20), nullable=False)  # 'Savings' or 'Current'
    balance = Column(Numeric(12, 2), nullable=False, default=0.00)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sender_account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
    receiver_account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    transaction_status = Column(String(20), default="SUCCESS")  # SUCCESS, FAILED, FLAGGED
    timestamp = Column(TIMESTAMP, server_default=func.now())

class FraudLog(Base):
    __tablename__ = "fraud_logs"

    fraud_log_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    transaction_id = Column(Integer, ForeignKey("transactions.transaction_id", ondelete="CASCADE"), nullable=False)
    risk_score = Column(Float, nullable=False)
    is_fraudulent = Column(Boolean, default=False)
    detected_at = Column(TIMESTAMP, server_default=func.now())