from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/Узнать больше о компании')
b4 = KeyboardButton('/загрузить')
b5 = KeyboardButton('/Тест Case_Lab')
#b4 = KeyboardButton('Поделиться номером телефона', request_contact=True)
#b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4, b5)