<<<<<<< HEAD
# WebApp-Scaffold
This is just a quick and dirty scaffolding of a webapp without anything important going on
=======
# Railway Backend Scaffold

Minimal FastAPI + PostgreSQL + worker scaffold intended to be expanded later.

## Architecture

```text
FastAPI
   |
   v
PostgreSQL
   ^
   |
Worker
```

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -e ".[dev]"
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

Run the worker separately:

```bash
python -m worker.main
```

## API endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | metadata |
| GET | `/health` | API process health only |
| GET | `/db-health` | PostgreSQL connectivity |
| POST | `/examples` | create a record |
| GET | `/examples` | list records |
| GET | `/examples/{id}` | retrieve a record |

Example:

```bash
curl -X POST http://127.0.0.1:8000/examples \
  -H "Content-Type: application/json" \
  -d '{"name":"hello"}'
```

## Database migrations

```bash
alembic upgrade head
alembic revision --autogenerate -m "description"
```

Tables are intentionally not created with `create_all()`; Alembic owns schema evolution.

## Tests

```bash
pytest
```

The initial tests do not require a running PostgreSQL instance.

## Railway deployment

Use one Railway project with three services: PostgreSQL, API, and Worker.

Railway PostgreSQL exposes `DATABASE_URL`; reference that value as `DATABASE_URL` in both the API and Worker services. This application normalizes Railway-style `postgresql://...` URLs for psycopg 3.

API start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Configure `/health` as the API service healthcheck path. Railway injects `PORT` and uses it for healthchecks.

Worker start command:

```bash
python -m worker.main
```

The worker does not need a public domain.

Run migrations against the production database before relying on new schema changes:

```bash
alembic upgrade head
```

Recommended production variables:

```text
DATABASE_URL=<reference to Railway PostgreSQL DATABASE_URL>
APP_ENV=production
LOG_LEVEL=INFO
```

## Current scope

No frontend, CORS policy, Redis, Celery/RQ, authentication, object storage, FITS processing, Docker, reverse proxy, or queue infrastructure is included yet.
>>>>>>> 6cb4ed9 (Initial commit)
