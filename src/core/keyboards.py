from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

increase_the_tariff = InlineKeyboardButton('✅ Повысить тариф', callback_data='increase_the_tariff')
want_butter = InlineKeyboardButton('✅ Хочу масла', callback_data='want_butter')
to_the_start = InlineKeyboardButton('✅ В начало', callback_data='to_the_start')

keyboard_for_recommendations = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, want_butter, to_the_start)

keyboard_for_butters_and_start = InlineKeyboardMarkup(row_width=1).add(want_butter, to_the_start)

keyboard_for_start = InlineKeyboardMarkup(row_width=1).add(to_the_start)

get_contact = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Отправить свой контакт', request_contact=True))
