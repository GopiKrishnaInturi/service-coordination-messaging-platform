# Service Coordination Messaging Platform

Distributed backend service coordination and asynchronous messaging platform built using Python, FastAPI, PostgreSQL, Docker, Redis, and scalable synchronization workflows.

## Features

- Distributed service communication
- Asynchronous backend coordination
- Inventory and order synchronization
- REST API orchestration
- Incremental update processing
- Backend throughput monitoring
- SQL synchronization workflows
- Dockerized deployment

## Run

```bash
docker-compose up --build
```

## APIs

- POST /orders
- POST /inventory/update
- POST /customers/register
- GET /synchronization/status
- GET /health