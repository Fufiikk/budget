import sqlite3 as sq
from create_bot import bot,dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import Dispatcher
from aiogram import types,Dispatcher
from inline_cb import kb_dell, kb_add
from sqlite_3_ import get_0

async def get_otvet_expenses_2():
    @dp.callback_query_handler(text='taxi')
    async def taxi(callback: types.CallbackQuery):
        # Удаляем предыдущее сообщение
        await get_0(callback)


    @dp.callback_query_handler(text='products')
    async def taxi(callback: types.CallbackQuery):
        # Удаляем предыдущее сообщение
        await get_0(callback)


    @dp.callback_query_handler(text='electronics')
    async def taxi(callback: types.CallbackQuery):
        # Удаляем предыдущее сообщение
        await get_0(callback)


    @dp.callback_query_handler(text='connection')
    async def taxi(callback: types.CallbackQuery):
        # Удаляем предыдущее сообщение
        await get_0(callback)


    @dp.callback_query_handler(text='other expenses')
    async def taxi(callback: types.CallbackQuery):
        # Удаляем предыдущее сообщение
        await get_0(callback)