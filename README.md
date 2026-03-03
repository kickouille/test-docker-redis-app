# Docker + Redis Web App

> 🤖 **This repository and application has been entirely created with AI (Claude) and MCP (Model Context Protocol) Tools.** No code was written manually - every file, commit and configuration was generated and pushed by an AI agent.

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

## 🤖 About AI & MCP Tools

This project was entirely created by an AI agent (Claude by Anthropic) using MCP (Model Context Protocol) Tools to interact with GitHub. This includes:
- Creating the GitHub repository
- Writing all application code
- Creating all configuration files
- Writing this documentation

No human wrote a single line of code or configuration!
