
from typing import Any, Union
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
import config
from aiogram import types
from datetime import datetime


class UserProviderMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, dp: Dispatcher):
        super(UserProviderMiddleware, self).__init__()
        self.dp = dp

    async def pre_process(self, message: Union[types.Message, types.CallbackQuery], data: dict, *agrs):
        data['user'] = await data['db_worker'].get_user(message.from_user.id)
        if not data['user']:
            await data['db_worker'].create_user(message.from_user.id, message.from_user.first_name, datetime.now())
            data['user'] = await data['db_worker'].get_user(message.from_user.id)
        



    
    async def post_process(self, obj, data, *args):
        if (data['user']):
            data['user'] = None