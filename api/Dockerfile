FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# ---- install deps ----
COPY api/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ---- copy app ----
COPY api ./api

# ---- run migrations + app ----
CMD ["sh", "-c", "cd /app/api && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]