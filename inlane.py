from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Клавиши
n_1 = InlineKeyboardButton(f'Дима лох!')

#Клавиатура
kb = InlineKeyboardMarkup(row_width=2)
kb.add(n_1)