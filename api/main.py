from typing import Optional

from fastapi import FastAPI

from database.get_conn import get_conn
from database.db_worker import DBWorker

from config import postgresql

app = FastAPI()


@app.get("/")
async def read_root():
    print("GET")
    conn = await get_conn(postgresql)
    db_worker = DBWorker(conn)
    a = await db_worker.get_all_tokens_output()
    return a


@app.delete("/{output_id}")
async def delete_token_output(output_id: int):
    print("DELETE")
    conn = await get_conn(postgresql)
    db_worker = DBWorker(conn)
    a = await db_worker.delete_tokens_output(output_id)
    return {"status": "ok"}