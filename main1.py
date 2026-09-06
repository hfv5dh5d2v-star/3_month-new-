import aiogram 
import logging
import asyncio
from aiogram import Bot, Dispatcher, Router
from config import BOT_TOKEN
from src.handlers import router


bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    # logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    asyncio.run(main())
    # logging.basicConfig(level=logging.INFO)