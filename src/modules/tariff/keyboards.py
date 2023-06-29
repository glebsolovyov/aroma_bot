from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

buy_base_tariff = InlineKeyboardButton('✅ Купить', callback_data='buy_base_tariff')
buy_base_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(buy_base_tariff)

buy_base_with_feedback_tariff = InlineKeyboardButton('✅ Купить', callback_data='buy_base_with_feedback')
buy_base_with_feedback_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(buy_base_with_feedback_tariff)

buy_mentoring_tariff = InlineKeyboardButton('✅ Купить', callback_data='buy_mentoring_tariff')
buy_mentoring_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(buy_mentoring_tariff)

get_contact = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Отправить свой контакт', request_contact=True))


get_email = InlineKeyboardButton('✅ Ввести email', callback_data='get_email')
get_email_keyboard = InlineKeyboardMarkup(row_width=1).add(get_email)
