import os

import psycopg2
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from Python CI/CD!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/employees")
def get_employees():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, role FROM employees ORDER BY id"
    )

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "role": row[2],
        }
        for row in rows
    ]