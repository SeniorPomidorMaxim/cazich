from aiogram import Dispatcher
from aiogram import Bot

from routers.router import start_router

TOKEN = '6320038176:AAGPJi3Qvpywmqiv2Pf6ComaOp33nvNHYCk'
bot = Bot(TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
