from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cluster_storage import SessionLocal
from contracts import OrderPayload, InventoryPayload
from message_broker import create_order, update_inventory

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orders")
def create_order_endpoint(payload: OrderPayload, db: Session = Depends(get_db)):
    return create_order(db, payload)

@router.post("/inventory/update")
def update_inventory_endpoint(payload: InventoryPayload, db: Session = Depends(get_db)):
    return update_inventory(db, payload)

@router.post("/customers/register")
def register_customer():
    return {"message": "Customer registered successfully"}

@router.get("/synchronization/status")
def synchronization_status():
    return {"synchronization": "stable"}

@router.get("/health")
def health():
    return {"status": "running"}