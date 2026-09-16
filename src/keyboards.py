from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


reply = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = 'Python'), 
                                        KeyboardButton(text = 'JavaScript')], 
                                        [KeyboardButton(text = 'Java')]
                                        ], resize_keyboard = True)

inline = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Python', url = 'https://docs.python.org/3/')],
    [InlineKeyboardButton(text = 'JavaScript', url = 'https://developer.mozilla.org/en-US/docs/Web/JavaScript')],
    [InlineKeyboardButton(text = 'Java', url = 'https://docs.oracle.com/en/java/')]
])

inline_1 = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text ='игра с менеджментом', callback_data='management_support')]
])