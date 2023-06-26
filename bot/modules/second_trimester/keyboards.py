from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

basic_rules_button = InlineKeyboardButton('✅ Основные правила использования эфирных масел.', callback_data='basic_rules2')
basic_rules_keyboard = InlineKeyboardMarkup(row_width=1).add(basic_rules_button)

next_basic_rules_button = InlineKeyboardButton('✅ Далее', callback_data='bothering')
next_basic_rules_keyboard = InlineKeyboardMarkup(row_width=1).add(next_basic_rules_button)

edema_button = InlineKeyboardButton('✅ Отеки', callback_data='edema')
back_pain_button = InlineKeyboardButton('✅ Боли в спине', callback_data='back_pain')
constipation_button = InlineKeyboardButton('✅ Запоры', callback_data='constipation')

bothering_keyboard = InlineKeyboardMarkup(row_width=1).add(edema_button, back_pain_button, constipation_button)

edema_increase_the_tariff_button = InlineKeyboardButton('✅ повысить тариф', callback_data='edema_increase_the_tariff')
edema_increase_the_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(edema_increase_the_tariff_button)



