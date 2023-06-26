from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

increase_the_tariff = InlineKeyboardButton('✅ Повысить тариф', callback_data='increase_the_tariff')
want_butter = InlineKeyboardButton('✅ Хочу масла', callback_data='want_butter')
to_the_start = InlineKeyboardButton('✅ В начало', callback_data='to_the_start')

keyboard_for_recommendations = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, want_butter, to_the_start)
