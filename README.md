# Docker + Redis Web App

A simple Python Flask web application using Redis as a hit counter, orchestrated with Docker Compose.

## Stack

| Component | Technology |
|-----------|------------|
| Web App   | Python / Flask / Gunicorn |
| Cache/DB  | Redis 7 (Alpine) |
| Container | Docker + Docker Compose |

## Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Run the app

```bash
# Clone the repo
git clone https://github.com/kickouille/test-docker-redis-app.git
cd test-docker-redis-app

# Build and start all services
docker compose up --build
```

Then open your browser at http://localhost:5000

### Stop the app

```bash
docker compose down
```

### Stop and remove volumes

```bash
docker compose down -v
```

## Endpoints

| Route | Description |
|-------|-------------|
| `GET /` | Main page - shows Redis hit counter |
| `GET /health` | Health check - pings Redis |

## Project Structure

```
.
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Web app Docker image
├── docker-compose.yml  # Multi-service orchestration
├── .dockerignore       # Docker build exclusions
└── README.md           # This file
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `REDIS_HOST` | `redis` | Redis hostname |
| `REDIS_PORT` | `6379`  | Redis port |
