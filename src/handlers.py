from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from src.keyboards import reply, inline, inline_1

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello, {message.from_user.
                                   full_name}! I am your bot.", reply_markup = reply)
    print(f' user {message.from_user.full_name}, \n his/her id {message.from_user.id}, \n his/her nickname {message.from_user.username} )')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("This is a help message. Use /start to start the bot.", reply_markup = inline_1)

@router.message(Command('docs'))
async def cmd_docs(message: Message):
    await message.answer("Выбери язык, чтобы перейти к официальной документации:", reply_markup = inline)

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer("This bot is created to demonstrate basic command handling using aiogram.")

@router.message(F.text == 'Python')
async def cmd_python(message: Message):
    await message.answer('Python - это высокоуровневый язык ' \
    'программирования с простым и понятным синтаксисом. Широко ' \
    'используется в веб-разработке, анализе данных, искусственном ' \
    'интеллекте, автоматизации и создании Telegram-ботов.')

@router.message(F.text == 'JavaScript')
async def cmd_javascript(message: Message):
    await message.answer('JavaScript - это главный язык веб-разработки, ' \
    'который исполняется прямо в браузере. Позволяет создавать ' \
    'интерактивные веб-страницы, а с помощью платформы Node.js ' \
    'используется и для написания серверной части приложений (backend). ')

@router.message(F.text == 'Java')
async def cmd_java(message: Message):
    await message.answer('Java - это строго типизированный о' \
    'бъектно-ориентированный язык программирования. ' \
    'Известен принципом «напиши один раз, запускай где угодно» '
    '(благодаря JVM). Активно используется в корпоративной разработке, ' \
    'банках и создании Android-приложений. ')

@router.callback_query(F.data == 'tech_support')
async def cmd_tech_support(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Вы выбрали техническую поддержку. " \
    "Пожалуйста, опишите вашу проблему.")

@router.callback_query(F.data == 'management_support')
async def cmd_management_support(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Вы выбрали управленческую поддержку. " \
    "Пожалуйста, опишите вашу проблему.")

@router.message()
async def echo(message: Message):
    await message.answer(f'You said: {message.text}')

@router.message(F.text.lower() == 'bye')
async def cmd_bye(message: Message):
    await message.answer("Goodbye! Have a great day!")