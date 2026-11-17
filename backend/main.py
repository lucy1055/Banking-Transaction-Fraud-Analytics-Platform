from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from decimal import Decimal

from . import database, models, crud

# Create database tables automatically if they don't exist
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Banking Transaction & Fraud Analytics API",
    description="High-concurrency banking engine with ACID compliance and fraud analytics.",
    version="1.0.0"
)

# Pydantic Schemas for Request Validation
class UserCreate(BaseModel):
    full_name: str
    email: str
    phone_number: str

class AccountCreate(BaseModel):
    user_id: int
    account_type: str  # 'Savings' or 'Current'
    initial_balance: Decimal

class TransferRequest(BaseModel):
    sender_id: int
    receiver_id: int
    amount: Decimal

@app.get("/")
def read_root():
    return {"message": "Welcome to the Banking Transaction & Fraud Analytics Platform API!"}

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, full_name=user.full_name, email=user.email, phone_number=user.phone_number)

@app.post("/accounts/")
def create_account(account: AccountCreate, db: Session = Depends(database.get_db)):
    return crud.create_account(db=db, user_id=account.user_id, account_type=account.account_type, initial_balance=account.initial_balance)

@app.post("/transfer/")
def transfer_funds(transfer: TransferRequest, db: Session = Depends(database.get_db)):
    result = crud.perform_transfer(db=db, sender_id=transfer.sender_id, receiver_id=transfer.receiver_id, amount=transfer.amount)
    if result["status"] != "SUCCESS":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.get("/accounts/{account_id}")
def get_account_details(account_id: int, db: Session = Depends(database.get_db)):
    account = crud.get_account(db=db, account_id=account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found.")
    return account