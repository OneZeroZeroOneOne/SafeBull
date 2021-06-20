from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from aiogram import types

from config import groups

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
        chat = None
        if isinstance(message, types.Message):
            chat = message.chat
        elif isinstance(message, types.CallbackQuery):
            chat = message.message.chat
        if chat:
            message.conf["is_private"] = True if chat.type == "private" else False
        else:
            message.conf["is_private"] = False
        message.conf["in_groups"] = True
        for i in groups:
            chat = await message.bot.get_chat(i)
            chat_member = await chat.get_member(message.from_user.id)
            if chat_member.status == "left":
                message.conf["in_groups"] = False
        return

    
