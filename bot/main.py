from math import floor
import time
from aiogram.dispatcher.dispatcher import Dispatcher
from logging import log
from typing import Dict, List
from yarl import URL
import asyncio
from aiogram import Bot
import config
from loguru import logger
import logging
from utils.intercept_standart_logger import InterceptStandartHandler
from utils.logs_writer import LogsWriterHandler
import threading
from aiogram.utils import executor
from bot import start_polling
from config import bot_token, postgresql
from database.get_conn import get_conn

def start():
    start_polling(bot_token, postgresql)


if __name__ == "__main__":
    logger.info(postgresql)
    conn = await get_conn(postgresql)
    import os
    if not os.path.exists("./logs"):
        os.mkdir("./logs")
    logging.basicConfig(handlers=[InterceptStandartHandler()], level=logging.WARN)
    handler = LogsWriterHandler()
    handler.log_date_file = floor(time.time())
    logger.add(handler)
    start()
