from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

next_start = InlineKeyboardButton('✅ Далее', callback_data='to_the_start')
next_start_keyboard = InlineKeyboardMarkup(row_width=1).add(next_start)
