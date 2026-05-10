# README.md
# Sea Freight Management System

This repository contains a simple microservice architecture for managing sea freight cargo. It includes:
- **API Gateway** (placeholder)
- **Cargo Service** (FastAPI)
- **Frontend** (Vue 3 + Vite)
- Docker configuration for each component

## Running locally

```bash
docker compose up --build
```

The services will be available at:
- API Gateway: http://localhost:8001
- Cargo Service: http://localhost:8000
- Frontend: http://localhost:5173

## Development

- Backend: `cd cargo-service && uvicorn main:app --reload`
- Frontend: `cd frontend && npm run dev`

