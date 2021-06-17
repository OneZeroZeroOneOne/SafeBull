from typing import Any, Type

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from asyncpg import Connection
from asyncpg.pool import Pool, PoolConnectionProxy

from aiogram import types

from loguru import logger
from database.db_worker import DBWorker



class DatabaseProviderMiddleware(LifetimeControllerMiddleware):
    """
    Database provider middleware middleware
    """
    
    skip_patterns = ["error", "update"]

    def __init__(self, dp: Dispatcher):
        super(DatabaseProviderMiddleware, self).__init__()
        self.dp = dp

    async def pre_process(self, message: types.CallbackQuery, data: dict, *agrs):
        pool: Pool = self.dp['db_pool']
        conn = await pool.acquire()
        data['db_conn'] = conn
        data['db_worker'] = DBWorker(data['db_conn'])
    
    async def post_process(self, obj, data: dict, *agrs):
        if data.get('db_worker'):
            data['db_worker'] = None
        if data.get('db_conn'):
            await self.dp['db_pool'].release(data['db_conn'])


            
