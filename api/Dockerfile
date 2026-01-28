FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Build context is ./api, so requirements.txt is at the root of the context
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole ./api context into /app/api so imports like "api.db..." work
COPY . ./api

CMD ["sh", "-c", "alembic -c api/alembic.ini upgrade head && uvicorn api.main:app --host 0.0.0.0 --port 8000"]