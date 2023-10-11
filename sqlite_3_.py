import sqlite3 as sq
from create_bot import bot,dp
from aiogram import types,Dispatcher
from inline_cb import kb_dell, kb_add, kb_back, kb_sure, kb_quit_fsm, kb_sure_2, kb_sure_3, kb_sure_4, kb_sure_5, \
    kb_sure_6, kb_sure_7
import pandas as pd

#ID_user
ID = None

# Создаем таблицу
def sql_start():
    global conn, cur
    conn = sq.connect('budget.db')
    cur = conn.cursor()
    if conn:
        print(f'Data base connect OK')
    # cur.execute('''CREATE TABLE IF NOT EXISTS bud
    #                 (Taxi REAL Products REAL Electronics REAL Connection REAL Other expenses REAL)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS bud
                    (Taxi INTEGER, 
                    Products INTEGER,
                    Electronics INTEGER,
                    Connection INTEGER,
                    Other_expenses INTEGER,
                    All_expenses INTEGER,
                    Time TEXT,
                    Id_user INTEGER,
                    First_name_user TEXT,
                    Username TEXT)''')

    conn.commit()
        # Сохраняем изменения





async def get_0(callback: types.CallbackQuery):
    # Получаем количество строк в таблице
    cur.execute('SELECT COUNT(*) FROM bud')
    num_rows = cur.fetchone()[0]

    if num_rows == 0:
        # В таблице нет данных, отправляем сообщение об отсутствии товара
        await callback.message.answer("Вы ещё не вносили сюда затрату.", reply_markup=kb_dell)


async def dell_one(callback: types.CallbackQuery):
    cur.execute(f'SELECT COUNT({callback}) FROM bud', (callback, ))

    # Сохраняем изменения
    conn.commit()


async def dell_bd(callback: types.CallbackQuery):
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.message.answer(f'Вы уверены?\nОчистятся все данные!', reply_markup=kb_sure)


#Декораторы

@dp.callback_query_handler(text='yes')
async def dell_bd_2(callback: types.CallbackQuery):
    cur.execute("DELETE FROM bud")
    conn.commit()
    await callback.message.answer(f'Данные удалены!', reply_markup=kb_dell)


@dp.callback_query_handler(text='no')
async def dell_bd_2(callback: types.CallbackQuery):
    await callback.message.answer(f'Данные не были очищены!', reply_markup=kb_dell)
#ТАКСИ
@dp.callback_query_handler(text='yes_2')
async def dell_taxi(callback: types.CallbackQuery):
    taxi_list = []
    all_budget_list = []
    for tax in cur.execute('SELECT taxi FROM bud').fetchall():
        taxi_list.append(tax[0])
    for all in cur.execute('SELECT all_expenses FROM bud').fetchall():
        all_budget_list.append(all[0])
    cur.execute(f"UPDATE bud SET All_expenses = {sum(all_budget_list) - sum(taxi_list)}")
    cur.execute(f"UPDATE bud SET All_expenses")
    cur.execute("UPDATE bud SET Taxi = 0;")
    conn.commit()


    await callback.message.answer(f'Расходы по такси🚖 успешно удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='no_2')
async def no_dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Расходы не были удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='taxi')
async def dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Вы уверены? Чтобы удалить расходы по категории такси🚖.', reply_markup=kb_sure_2)
#ТАКСИ

#ПРОДУКТЫ

@dp.callback_query_handler(text='yes_3')
async def dell_taxi(callback: types.CallbackQuery):
    products_list = []
    all_budget_list = []
    for prod in cur.execute('SELECT products FROM bud').fetchall():
        products_list.append(prod[0])
    for all in cur.execute('SELECT all_expenses FROM bud').fetchall():
        all_budget_list.append(all[0])
    cur.execute(f"UPDATE bud SET All_expenses = {sum(all_budget_list) - sum(products_list)}")
    cur.execute("UPDATE bud SET Products = 0;")
    conn.commit()

    await callback.message.answer(f'Расходы по продукты🍔 успешно удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='no_3')
async def no_dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Расходы не были удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='products')
async def dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Вы уверены? Чтобы удалить расходы по категории продукты🍔.', reply_markup=kb_sure_3)

#ПРОДУКТЫ

#ЭЛЕКТРОНИКА
@dp.callback_query_handler(text='yes_4')
async def dell_taxi(callback: types.CallbackQuery):
    electronics_list = []
    all_budget_list = []
    for elec in cur.execute('SELECT electronics FROM bud').fetchall():
        electronics_list.append(elec[0])
    for all in cur.execute('SELECT all_expenses FROM bud').fetchall():
        all_budget_list.append(all[0])
    cur.execute(f"UPDATE bud SET All_expenses = {sum(all_budget_list) - sum(electronics_list)}")
    cur.execute("UPDATE bud SET Electronics = 0;")
    conn.commit()

    await callback.message.answer(f'Расходы по электроники💻 успешно удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='no_4')
async def no_dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Расходы не были удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='electronics')
async def dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Вы уверены? Чтобы удалить расходы по категории электроники💻.',
                                  reply_markup=kb_sure_4)
#ЭЛЕКТРОНИКА

#СВЯЗЬ
@dp.callback_query_handler(text='yes_5')
async def dell_taxi(callback: types.CallbackQuery):
    connection_list = []
    all_budget_list = []
    for conne in cur.execute('SELECT connection FROM bud').fetchall():
        connection_list.append(conne[0])
    for all in cur.execute('SELECT all_expenses FROM bud').fetchall():
        all_budget_list.append(all[0])
    cur.execute(f"UPDATE bud SET All_expenses = {sum(all_budget_list) - sum(connection_list)}")
    cur.execute("UPDATE bud SET Connection = 0;")
    conn.commit()

    await callback.message.answer(f'Расходы по связи📞 успешно удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='no_5')
async def no_dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Расходы не были удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='connection')
async def dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Вы уверены? Чтобы удалить расходы по категории связи📞.',
                                  reply_markup=kb_sure_5)
#СВЯЗЬ

#ДРУГИЕ РАСХОДЫ
@dp.callback_query_handler(text='yes_6')
async def dell_taxi(callback: types.CallbackQuery):
    other_expenses_list = []
    all_budget_list = []
    for all in cur.execute('SELECT all_expenses FROM bud').fetchall():
        all_budget_list.append(all[0])
    cur.execute(f"UPDATE bud SET All_expenses = {sum(all_budget_list) - sum(other_expenses_list)}")
    cur.execute("UPDATE bud SET Other_expenses = 0;")
    conn.commit()

    await callback.message.answer(f'Расходы по прочие расходы💳 успешно удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='no_6')
async def no_dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Расходы не были удалены!', reply_markup=kb_dell)

@dp.callback_query_handler(text='other expenses')
async def dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Вы уверены? Чтобы удалить расходы по категории прочие расходы💳.',
                                  reply_markup=kb_sure_6)

#ДРУГИЕ РАСХОДЫ

async def get_product(callback: types.CallbackQuery):
        taxi_list = []
        products_list = []
        electronics_list = []
        connection_list = []
        other_expenses_list = []
        all_budget_list = []
        for tax in cur.execute('SELECT taxi FROM bud').fetchall():
            taxi_list.append(tax[0])
        for prod in cur.execute('SELECT products FROM bud').fetchall():
            products_list.append(prod[0])
        for elec in cur.execute('SELECT electronics FROM bud').fetchall():
            electronics_list.append(elec[0])
        for conne in cur.execute('SELECT connection FROM bud').fetchall():
            connection_list.append(conne[0])
        for other in cur.execute('SELECT other_expenses FROM bud').fetchall():
            other_expenses_list.append(other[0])
        for all in cur.execute('SELECT all_expenses FROM bud').fetchall():
            all_budget_list.append(all[0])

        await bot.send_message(callback.from_user.id, f'Всего потрачено💰: {sum(all_budget_list)}₽\n\nТакси🚖:'
                                                      f' {sum(taxi_list)}₽\nПродукты🍔:'
                                                      f' {sum(products_list)}₽\nЭлектроника💻:'
                                                      f' {sum(electronics_list)}₽\n'
                                                      f'Связь📞: {sum(connection_list)}₽\nДругие расходы💳: '
                                                      f'{sum(other_expenses_list)}₽',
                               reply_markup=kb_back)

async def get_all_product(data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10):
    cur.execute("INSERT INTO bud (Taxi, Products, Electronics, Connection, Other_expenses, All_expenses, Time, "
                "Id_user, First_name_user, Username"
                ") VALUES (?, "
                "?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10))
    conn.commit()

@dp.callback_query_handler(text='yes_7')
async def get_exsel(callback: types.CallbackQuery):
    await callback.message.answer(f'Данные внесены!', reply_markup=kb_back)
    df = pd.read_sql('select * from bud', conn)
    df.to_excel(r'C:\Users\Дом\OneDrive\Рабочий стол\budget_exsel.xlsx', index=False)


@dp.callback_query_handler(text='add_exsel')
async def get_sure(callback: types.CallbackQuery):
    await callback.message.answer(f'Вы уверены?', reply_markup=kb_sure_7)


@dp.callback_query_handler(text='no_7')
async def no_dell_taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Данные не были внесены!', reply_markup=kb_dell)