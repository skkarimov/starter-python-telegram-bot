import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from configurator import config, make_config
from db import Database

# Configure logging
logging.basicConfig(level=logging.INFO)

if not make_config("config.ini"):
    logging.error("Errors while parsing config file. Exiting.")
    exit(1)


if not config.bot.token:
    logging.error("No token provided")
    exit(1)

# Initialize bot and dispatcher
bot = Bot(token=config.bot.token, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('db.db')
