from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

order_butter_button = InlineKeyboardButton('✅ Заказать', callback_data='order_butter')
order_butter_keyboard = InlineKeyboardMarkup(row_width=1).add(order_butter_button)
