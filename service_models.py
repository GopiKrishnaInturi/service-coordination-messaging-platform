from sqlalchemy import Column, Integer, String, Float, DateTime
from cluster_storage import Base
import datetime

class OrderRecord(Base):
    __tablename__ = "order_records"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    customer_name = Column(String)
    order_total = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class InventoryRecord(Base):
    __tablename__ = "inventory_records"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    quantity = Column(Integer)
    warehouse = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)