from aiogram.utils import executor
from create_bot import dp
from sqlite_3_ import sql_start
from handlers import client


async def on_srart_up(_):
    """FUFIIKK"""
    print(f"Бот вошёл в работу")
from handlers import client
client.register_handlers_clients(dp)

sql_start()



if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_srart_up)