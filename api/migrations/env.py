from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Ensure /app is on PYTHONPATH
sys.path.append("/app")

from api.db.models import Base  # ← this WILL work now

config = context.config

database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is not set")

config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata