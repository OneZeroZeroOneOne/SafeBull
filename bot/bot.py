from handlers.filters.ban_fiter import BanFilter
from middlewares.rule_checker_middleware import RuleCheckerMiddleware
from handlers.register_handlers import register_handlers
from middlewares.user_provider_middleware import UserProviderMiddleware
from middlewares.i18n_data_provider_midleware import I18nDataProviderMiddleware
from database.get_pool import get_pool
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from database.get_conn import get_conn

from middlewares.database_provider_middleware import DatabaseProviderMiddleware

from loguru import logger

def init_bot(token: str):
    return Bot(token=token, parse_mode='HTML')


def init_dispatcher(bot: Bot):
    storage = MemoryStorage()

    return Dispatcher(bot, storage=storage)



async def on_startup(dp: Dispatcher):
    logger.info("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    logger.info(dp["connection_string"])
    conn = await get_conn(dp["connection_string"])

    dp["db_pool"] = await get_pool(
        dp["connection_string"],
)


def start_polling(token: str, postgres: str):
    
    bot = init_bot(token)
    dp = init_dispatcher(bot)

    dp["connection_string"] = postgres

    dp.filters_factory.bind(BanFilter, event_handlers=[
        dp.callback_query_handlers,
        dp.message_handlers,
        dp.errors_handlers,
        dp.inline_query_handlers
    ])
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(DatabaseProviderMiddleware(dp))
    dp.middleware.setup(UserProviderMiddleware(dp))
    dp.middleware.setup(I18nDataProviderMiddleware(dp))
    dp.middleware.setup(RuleCheckerMiddleware(dp))
    
    register_handlers(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

