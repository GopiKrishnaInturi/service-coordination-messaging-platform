from fastapi import FastAPI
from connectors import router

app = FastAPI(title="Service Coordination Messaging Platform")

app.include_router(router)