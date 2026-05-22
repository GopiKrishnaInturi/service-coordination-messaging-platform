import random
from cluster_storage import SessionLocal
from service_models import OrderRecord

db = SessionLocal()

statuses = ["PROCESSING", "COMPLETED", "FAILED"]

for i in range(200):
    order = OrderRecord(
        order_id=f"ORD-{i}",
        customer_name=f"Customer-{i}",
        order_total=random.uniform(100, 2000),
        status=random.choice(statuses)
    )
    db.add(order)

db.commit()

print("Sample coordination workload generated")