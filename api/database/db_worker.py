from asyncpg.connection import Connection 

class DBWorker:
    def __init__(self, conn: Connection):
        self.conn = conn
    
    async def get_all_tokens_output(self):
        sql = """select tot."id", u."id" as user_id, tot.tokens ,tot.created_date_time from "tokens_output" tot join "user" u on tot.user_id = u."id" """
        return await self.conn.fetch(sql)
    
    async def delete_tokens_output(self, id):
        sql = "delete from \"tokens_output\" where \"id\" = $1" 
        return await self.conn.fetch(sql, id)
    
    
    