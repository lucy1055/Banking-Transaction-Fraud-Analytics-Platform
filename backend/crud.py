from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models
from decimal import Decimal

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.account_id == account_id).first()

def create_user(db: Session, full_name: str, email: str, phone_number: str):
    db_user = models.User(full_name=full_name, email=email, phone_number=phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_account(db: Session, user_id: int, account_type: str, initial_balance: Decimal):
    db_account = models.Account(user_id=user_id, account_type=account_type, balance=initial_balance)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def perform_transfer(db: Session, sender_id: int, receiver_id: int, amount: Decimal):
    """
    ACID-compliant fund transfer with row-level locking to prevent race conditions.
    """
    try:
        # Lock rows to prevent concurrent balance modifications
        sender = db.query(models.Account).filter(models.Account.account_id == sender_id).with_for_update().first()
        receiver = db.query(models.Account).filter(models.Account.account_id == receiver_id).with_for_update().first()

        if not sender or not receiver:
            return {"status": "FAILED", "message": "Sender or Receiver account not found."}

        if sender.balance < amount:
            return {"status": "FAILED", "message": "Insufficient balance."}

        # Perform debit and credit
        sender.balance -= amount
        receiver.balance += amount

        # Record transaction
        db_transaction = models.Transaction(
            sender_account_id=sender_id,
            receiver_account_id=receiver_id,
            amount=amount,
            transaction_status="SUCCESS"
        )
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)

        return {
            "status": "SUCCESS",
            "transaction_id": db_transaction.transaction_id,
            "message": "Transfer completed successfully."
        }
    except Exception as e:
        db.rollback()
        return {"status": "ERROR", "message": str(e)}