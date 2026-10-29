import os

# Keep unit tests independent from a running PostgreSQL server and psycopg.
os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///:memory:")
