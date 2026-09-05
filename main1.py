import aiogram 
import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import BOT_TOKEN


bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello, {message.from_user.
                                   full_name}! I am your bot.")
    print(f' user {message.from_user.full_name}, \n his/her id {message.from_user.id}, \n his/her nickname {message.from_user.username} )')

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("This is a help message. Use /start to start the bot.")

@dp.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer("This bot is created to demonstrate basic command handling using aiogram.")



@dp.message()
async def echo(message: Message):
    await message.answer(f'You said: {message.text}')

@dp.message(F.text.lower() == 'bye')
async def cmd_bye(message: Message):
    await message.answer("Goodbye! Have a great day!")
    

async def main():
    await dp.start_polling(bot)
    # logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    asyncio.run(main())
    # logging.basicConfig(level=logging.INFO)