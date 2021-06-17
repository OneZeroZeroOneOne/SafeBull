from asyncpg.connection import Connection 

class DBWorker:
    def __init__(self, conn: Connection):
        self.conn = conn
    
    async def get_all_tokens_output(self):
        sql = "select * from \"tokens_output\""
        return await self.conn.fetch(sql)
    
    async def delete_tokens_output(self, id):
        sql = "delete from \"tokens_output\" where \"id\" = $1" 
        return await self.conn.fetch(sql, id)
    
    
    