from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from src.keyboards import reply, inline, inline_1
from src.questions import QUESTIONS
from db.users import create_user, get_user, get_all_users, delete_user

router = Router()

class Manage_Support(StatesGroup):
    waiting_answer = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = create_user(
        username=message.from_user.full_name or 'User Unknown',
        telegram_id=message.from_user.id
    )
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


#FSM

@router.callback_query(F.data == 'management_support')
async def cmd_management_support(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(index = 0, score = 0)
    await state.set_state(Manage_Support.waiting_answer)
    await callback.message.answer(QUESTIONS[0]['question'])

@router.message(Manage_Support.waiting_answer)

async def user_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index= data['index']
    score = data['score']
    if message.text.lower() == QUESTIONS[index]['answer']:
        score += 1
        await message.answer('Правильный ответ!')
    else:
        await message.answer(f'Ответ не верен, правильный ответ:{QUESTIONS[index]['answer'].lower()}')
    
    
    index += 1

    len_q = len(QUESTIONS)

    if index == len_q:
        await message.answer(f'Игра окончена! ваш Счет {score}/{index}\nХочещь сыграть еще?', reply_markup = inline_1)
        await state.clear
    else:
        await state.update_data(index = index, score = score)
        await message.answer(f'Вопрос {index + 1} : ' + QUESTIONS[index]['question'])


@router.message(Command('users'))
async def cmd_users(message: Message):
    users = get_all_users()
    if not users:
        await message.answer('В базе данных пока нет пользователей')
        return
    text = 'Список пользователей:\n\n'
    for user in users:
        text += f'ID: {user['id']}\n'
        text += f'Username: {user['username']}\n'
        text += f'Telegram ID: {user['telegram_id']}\n'

    await message.answer(text)

@router.message(Command('delete'))
async def cnd_delete(message: Message):
    user = get_user(message.from_user.id)

    if not user:
        await message.answer('Вас нет в базе данных')
        return

    delete_user(message.from_user.id)
    await message.answer("Вы успешно удалены из базы данных.")


@router.message()
async def echo(message: Message):
    await message.answer(f'You said: {message.text}')

@router.message(F.text.lower() == 'bye')
async def cmd_bye(message: Message):
    await message.answer("Goodbye! Have a great day!")