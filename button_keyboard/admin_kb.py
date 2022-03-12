from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b_load = KeyboardButton('/Загрузить стажировку')
b_delete = KeyboardButton('/Удалить стажировку')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(b_load, b_delete)


