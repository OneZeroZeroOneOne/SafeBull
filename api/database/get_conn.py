import asyncpg

async def get_conn(connection_string: str):
    a = await asyncpg.connect(dsn=connection_string)
    return a