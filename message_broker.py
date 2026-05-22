from sqlalchemy.orm import Session
from service_models import OrderRecord, InventoryRecord

def create_order(db: Session, payload):
    order = OrderRecord(**payload.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def update_inventory(db: Session, payload):
    inventory = InventoryRecord(**payload.dict())
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory