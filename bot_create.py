from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token='5219280214:AAGicO98Bv4bDm2IHSHQvRz7yw91lGoaHmA')
dp = Dispatcher(bot, storage=storage)