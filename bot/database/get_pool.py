import asyncpg

async def get_pool(connection_string: str):
    a = await asyncpg.create_pool(dsn=connection_string)
    return a