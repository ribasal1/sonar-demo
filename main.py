import sqlite3

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/user/{user_id}")
def get_user(user_id: str):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT name, email FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return {"results": rows}