from typing import Any, Type

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from asyncpg import Connection

from aiogram import types

from loguru import logger
from database.db_worker import DBWorker
from config import groups, group_leave_timeout_sec
import datetime

class RuleCheckerMiddleware(LifetimeControllerMiddleware):

    skip_patterns = ["error", "update"]

    def __init__(self, dp: Dispatcher):
        super(RuleCheckerMiddleware, self).__init__()
        self.dp = dp

    async def pre_process(self, message: types.CallbackQuery, data: dict, *agrs):
        if data['user']['begin_captcha'] and data['user']['accept_rules']:
            message.conf["has_rights"] = True
        else:
            message.conf["has_rights"] = False
        message.conf["is_banned"] = data['user']['is_banned']
        #res = await data['db_worker'].get_last_subscribe_check(message.from_user.id)
        message.conf["in_groups"] = True
        for i in groups:
            chat = await message.bot.get_chat(i)
            chat_member = await chat.get_member(message.from_user.id)
            if chat_member.status == "left":
                message.conf["in_groups"] = False
        return

    
