from cluster_storage import Base, engine
from service_models import OrderRecord, InventoryRecord

Base.metadata.create_all(bind=engine)

print("Coordination platform database initialized")