import os
import psycopg
from pgvector.psycopg import register_vector
from dotenv import load_dotenv

load_dotenv()

def test_db():
    conn_str = os.getenv("DATABASE_URL")
    with psycopg.connect(conn_str) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.execute("SELECT extversion FROM pg_extension WHERE extname = 'vector';")
            version = cur.fetchone()
            print(f"Подключение успешно! Версия pgvector: {version[0]}")

if __name__ == "__main__":
    test_db()
