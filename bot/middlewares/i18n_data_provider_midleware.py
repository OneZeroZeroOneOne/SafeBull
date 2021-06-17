from typing import Any
from aiogram.types import Update

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from config import DEFAULT_LANG, Lang, texts


class I18nDataProviderMiddleware(LifetimeControllerMiddleware):
    def __init__(self, dp: Dispatcher):
        super(I18nDataProviderMiddleware, self).__init__()
        self.dp = dp

    async def pre_process(self, message: Any, data: dict, *args):
        if (isinstance(message, Update)): return
        user = data.get("user")
        if (user):
            data['_'] = texts[Lang(user["lang_id"]).name]
        else:
            data['_'] = texts[DEFAULT_LANG.name]
