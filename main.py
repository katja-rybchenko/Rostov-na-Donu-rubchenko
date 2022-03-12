from aiogram.utils import executor
from bot_create import dp
from basa_d import sql_bd

async def on_startup(_):
    print('Бот в онлайне')
    sql_bd.sql_start()
from Обработчики import work_with_client, admin_work, additional_features

work_with_client.register_handler_client(dp)
admin_work.register_handler_admin(dp)
additional_features.register_handler_antimat(dp) # импортировать последним

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
