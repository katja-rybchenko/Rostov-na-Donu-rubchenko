from bot_create import dp, bot
from aiogram import Dispatcher, types
from button_keyboard import kb_client
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

class Test(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()


@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'хОРОШЕГО ДНЯ', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишите ему:\nhttps://t.me/Case_Lab_Bot')

@dp.message_handler(commands=['Узнать больше о компании'])
async def command_now(message : types.Message):
    await bot.send_message(message.from_user.id, f'''В этом разделе пока нет информации ''', reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['Тест Case_Lab'], state=None)
async def command_test(message : types.Message):
    await Test.question1.set()
    await message.reply('Какие языки программирования вы знаете?')


#1
@dp.message_handler(content_types=['question1'], state=Test.question1)
async def load_question1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['question1'] = message.text
        await Test.next()
        await message.reply('Есть ли у вас начальные знания Unix Linux?')
#2
@dp.message_handler(content_types=['question2'], state=Test.question2)
async def load_question2(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['question2'] = message.text
        await Test.next()
        await message.reply('Умеете ли вы работать с офисным ПО(Excel, Word, Outlook, PowerPoint?')

#3
@dp.message_handler(content_types=['question3'], state=Test.question3)
async def load_question3(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['question3'] = message.text
        await Test.next()
        await message.reply('Есть ли у вас навыки проектирования БД SQL ?')

#4
@dp.message_handler(state=Test.question4)
async def load_question4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question4'] = message.text
    await state.finish()

@dp.message_handler(state='*', commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_stop(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')




def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_now, commands=['Узнать больше о компании'])
    dp.register_message_handler(command_test, commands=['Тест Case_Lab'], state=None)
    dp.register_message_handler(load_question1, content_types=['question1'], state=Test.question1)
    dp.register_message_handler(load_question2, content_types=['question2'], state=Test.question2)
    dp.register_message_handler(load_question3, content_types=['question3'], state=Test.question3)
    dp.register_message_handler(load_question4, content_types=['question4'], state=Test.question4)
    dp.register_message_handler(cancel_stop, state='*', commands='отмена')
    dp.register_message_handler(cancel_stop, Text(equals='отмена', ignore_case=True), state="*")
