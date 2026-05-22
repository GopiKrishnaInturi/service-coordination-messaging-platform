from pydantic import BaseModel

class OrderPayload(BaseModel):
    order_id: str
    customer_name: str
    order_total: float
    status: str

class InventoryPayload(BaseModel):
    product_name: str
    quantity: int
    warehouse: str