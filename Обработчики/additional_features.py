from aiogram import types, Dispatcher
import string
from bot_create import dp


#@dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation))for i in message.text.split(' ')}.intersection({'блядь', 'ебать', 'пизда', 'сука', 'хуй'}) != set():
        await message.reply('Без матов в чате!!!')
        await message.delete()


def register_handler_antimat(dp : Dispatcher):
    dp.register_message_handler(echo_send)