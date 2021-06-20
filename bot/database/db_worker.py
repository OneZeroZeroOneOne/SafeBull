from asyncpg.connection import Connection 

class DBWorker:
    def __init__(self, conn: Connection):
        self.conn = conn
    

    async def create_user(self, user_id, name, created_date_time):
        sql = "insert into \"user\"(\"id\",\"name\",\"created_date_time\") values($1, $2, $3) on conflict do nothing returning \"id\""
        row = await self.conn.fetchrow(sql, user_id, name, created_date_time)
        if row:
            return row['id']
        return None
    
    async def get_user(self, user_id):
        sql = "select * from \"user\" where \"id\" = $1"
        info = await self.conn.fetchrow(sql, user_id)
        return info

    async def add_refferrer_id(self, user_id, refferrer_id):
        sql = "update \"user\" set \"refferrer_id\" = $1 where \"id\" = $2"
        await self.conn.execute(sql, refferrer_id, user_id)
    
    async def set_user_lang(self, lang_id, user_id):
        sql = "update \"user\" set \"lang_id\" = $1 where \"id\" = $2"
        await self.conn.execute(sql, lang_id, user_id)

    async def ban_user(self, user_id):
        sql = "update \"user\" set \"is_banned\" = $1 where \"id\" = $2"
        await self.conn.execute(sql, True, user_id)

    async def set_accept_rule(self, user_id):
        sql = "update \"user\" set \"accept_rules\" = $1 where \"id\" = $2"
        await self.conn.execute(sql, True, user_id)

    async def set_confirm_captcha(self, user_id):
        sql = "update \"user\" set \"begin_captcha\" = $1 where \"id\" = $2"
        await self.conn.execute(sql, True, user_id)

    async def get_last_subscribe_check(self, user_id):
        sql = "select * from \"group_activity\" where \"user_id\" = $1"
        info = await self.conn.fetchrow(sql, user_id)
        return info
    
    async def set_bep_address(self, address, user_id):
        sql = "update \"user\" set \"bep_address\" = $1 where \"id\" = $2"
        await self.conn.execute(sql, address, user_id)
    
    async def get_invite_accruals(self, inviter_id, invited_id):
        sql = "select * from \"invite_accruals\" where \"inviting_user_id\" = $1 and  \"invited_id\" = $2"
        return await self.conn.fetchrow(sql, inviter_id, invited_id)
    
    
    async def add_token_for_user(self, user_id, tokens: int):
            sql = "update \"user\" set \"tokens\" = \"tokens\" + $1 where \"id\" = $2"
            await self.conn.execute(sql, tokens, user_id)

    async def add_invite_accruals(self, inviter_id, invited_id, created_date_time, tokens: int):
        sql = "insert into \"invite_accruals\"(\"inviting_user_id\",\"invited_id\",\"created_date_time\",\"tokens\") values($1, $2, $3, $4) on conflict do nothing"
        row = await self.conn.execute(sql, inviter_id, invited_id, created_date_time, tokens)
    

    async def get_tokens_output(self, user_id):
        sql = "select * from \"tokens_output\" where \"user_id\" = $1"
        return await self.conn.fetchrow(sql, user_id)
    
    async def add_tokens_output(self, user_id, created_date_time, tokens: int):
        sql = "insert into \"tokens_output\"(\"user_id\", \"created_date_time\", \"tokens\") values($1, $2, $3) on conflict do nothing returning \"id\""
        row = await self.conn.fetchrow(sql, user_id, created_date_time, tokens)
        if row:
            return row['id']
        return None
    
    async def minus_user_tokens(self, user_id, tokens: int):
        sql = "update \"user\" set \"tokens\" = \"tokens\" - $2 where \"id\" = $1"
        await self.conn.execute(sql, user_id, tokens)
    
    async def get_user_invite_accruals(self, user_id):
        sql = "select * from \"invite_accruals\" where \"inviting_user_id\" = $1"
        return await self.conn.fetch(sql, user_id)
    
    
    