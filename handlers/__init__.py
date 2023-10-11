from handlers import client



# @dp.callback_query_handler(text='expenses_2')
# async def get_otvet(callback: types.CallbackQuery):
#     # Удаляем предыдущее сообщение
#     await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
#     await callback.message.answer(f'По какой категории интересуют затраты?',reply_markup=kb_2)
#     callback_data = callback.data
#     if callback_data == 'expenses_2':
#         @dp.callback_query_handler(text='taxi')
#         async def taxi(callback: types.CallbackQuery):
#             # Удаляем предыдущее сообщение
#             await get_0(callback)
#
#         @dp.callback_query_handler(text='products')
#         async def taxi(callback: types.CallbackQuery):
#             # Удаляем предыдущее сообщение
#             await get_0(callback)
#
#         @dp.callback_query_handler(text='electronics')
#         async def taxi(callback: types.CallbackQuery):
#             # Удаляем предыдущее сообщение
#             await get_0(callback)
#
#         @dp.callback_query_handler(text='connection')
#         async def taxi(callback: types.CallbackQuery):
#             # Удаляем предыдущее сообщение
#             await get_0(callback)
#
#         @dp.callback_query_handler(text='other expenses')
#         async def taxi(callback: types.CallbackQuery):
#             # Удаляем предыдущее сообщение
#             await get_0(callback)