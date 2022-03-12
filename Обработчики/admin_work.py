from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot_create import dp, bot
from aiogram.dispatcher.filters import Text
from basa_d import sql_bd
from button_keyboard import admin_kb


ID = None

class Admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


@dp.message_handler(commands=['мод'], is_chat_admin=True)
async def make_commands(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Поле работы администратора', reply_markup=admin_kb.button_case_admin)
    await message.delete()


@dp.message_handler(commands='загрузить', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await Admin.photo.set()
        await message.reply('Загрузить фото')


# 1
@dp.message_handler(content_types=['photo'], state=Admin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await Admin.next()
        await message.reply('Теперь введи название')


# 2
@dp.message_handler(state=Admin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await Admin.next()
        await message.reply('Теперь описание')


# 3
@dp.message_handler(state=Admin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await Admin.next()
        await message.reply('Теперь цена')


@dp.message_handler(state=Admin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text
        await sql_bd.sql_add_interns(state)
        await state.finish()


@dp.message_handler(state='*', commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=Admin.photo)
    dp.register_message_handler(load_name, state=Admin.name)
    dp.register_message_handler(load_description, state=Admin.description)
    dp.register_message_handler(load_price, state=Admin.price)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(make_commands, commands=['мод'], is_chat_admin=True)