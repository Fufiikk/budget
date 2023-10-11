from inline_cb import kb,kb_2, kb_dell_2, kb_back_menu, kb_quit_fsm, kb_dell_cat
from sqlite_3_ import get_0, dell_bd, get_product, get_all_product, get_exsel
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram import types,Dispatcher
from create_bot import dp, bot
from inline_cb import kb_2, kb_adm
from datetime import datetime
from dadata import Dadata




async def get_menu(message: types.Message):
    await message.answer(f'{message.from_user.first_name} приветствую!\nВыберите нужное действие:',
                                 reply_markup=kb)

async def get_adm_menu(message: types.Message):
    ID = message.from_user.id
    if ID == 5967894458:
        await message.answer(f'Здравствуй. Вот твои возможности:', reply_markup=kb_adm)
    else:
        await message.answer(f'Простите, но вы не являетесь администратором.')


@dp.callback_query_handler(text='end')
async def get_otvet_2(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(f'{callback.message.chat.first_name} приветствую!\nВот список моих возможностей:',
                                          reply_markup=kb)


@dp.callback_query_handler(text='dell_3')
async def dell_cat(callback: types.CallbackQuery):
    await callback.message.answer(f'По какой категории желаете удалить расходы?', reply_markup=kb_dell_cat)
@dp.callback_query_handler(text='dell')
async def get_otvet_3(callback: types.CallbackQuery):
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)





@dp.callback_query_handler(text='expenses_1')
async def get_otvet_4(callback: types.CallbackQuery):
    ID = callback.from_user.id
    if ID == 5967894458:
            await get_product(callback)
    else:
        await callback.message.answer(f'Доступ запрещён!!!')


@dp.callback_query_handler(text='changes')
async def get_otvet_5(callback: types.CallbackQuery):
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
            await callback.message.answer(f'Какие хотите внести изменения?', reply_markup=kb_dell_2)

@dp.callback_query_handler(text='dell_2')
async def dell_full_bd(callback: types.CallbackQuery):
            await dell_bd(callback)


@dp.callback_query_handler(text="quit_fsm", state="*")
async def exit_state(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(f'{callback.from_user.first_name} приветствую!\nВыберите нужное действие:',
                                 reply_markup=kb)


class Budget_fsm(StatesGroup):
    money = State()
    taxi = State()
    products = State()
    electronics = State()
    connection = State()
    other_expenses = State()

@dp.callback_query_handler()
async def get_money_categories(callback: types.CallbackQuery):
    ID = callback.from_user.id
    if ID == 5967894458:
            if callback.data == 'expenses_2':
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
                await callback.message.answer(f'Чтобы добавить нажмите на - Добавить💼\nЕсли не желаете добавлять расход '
                                              f'указывайте '
                                              f'0.\nСтрого указывать числа. Без текста.\n'
                                              f'Если вы ввели текст, то нажмите на кнопку "Выйти⛔" и повторите попытку заново.',
                                              reply_markup=kb_2)
            elif callback.data == 'add_categories':
                await callback.message.answer(f'Введите значение для такси🚖:', reply_markup=kb_quit_fsm)
                await Budget_fsm.taxi.set()
    else:
        await callback.message.answer(f'Доступ запрещён!!!')




@dp.message_handler(state=Budget_fsm.taxi)
async def get_taxi(message: types.Message, state: FSMContext):
            await state.update_data(taxi=message.text)
            await Budget_fsm.products.set()
            await message.answer(f'Введите значение для продуктов🍔:', reply_markup=kb_quit_fsm)



@dp.message_handler(state=Budget_fsm.products)
async def get_taxi(message: types.Message, state: FSMContext):
            await state.update_data(products=message.text)
            await Budget_fsm.electronics.set()
            await message.answer(f'Введите значение для электроники💻:', reply_markup=kb_quit_fsm)





@dp.message_handler(state=Budget_fsm.electronics)
async def get_taxi(message: types.Message, state: FSMContext):
            await state.update_data(electronics=message.text)
            await Budget_fsm.connection.set()
            await message.answer(f'Введите значение для связи📞:', reply_markup=kb_quit_fsm)




@dp.message_handler(state=Budget_fsm.connection)
async def get_taxi(message: types.Message, state: FSMContext):
            await state.update_data(connection=message.text)
            await Budget_fsm.other_expenses.set()
            await message.answer(f'Введите значение для прочих расходов💳:', reply_markup=kb_quit_fsm)



@dp.message_handler(state=Budget_fsm.other_expenses)
async def get_taxi(message: types.Message, state: FSMContext):
    await state.update_data(other_expenses=message.text)
    data = await state.get_data()
    data_time = datetime.now()
    int_data = float(data['taxi'])+float(data['products'])+float(data['electronics'])+float(data['connection'])+\
                       float(data['other_expenses'])
    await get_all_product(data['taxi'], data['products'], data['electronics'], data['connection'],
                                  data['other_expenses'], int_data, data_time, message.from_user.id,
                                  message.from_user.first_name, message.from_user.username)

    await message.answer(f'Все данные внесены успешно', reply_markup=kb_back_menu)
    await state.finish()















def register_handlers_clients(dp: Dispatcher):
    dp.register_message_handler(get_menu, commands='start')
    dp.register_message_handler(get_adm_menu, commands='adm')
