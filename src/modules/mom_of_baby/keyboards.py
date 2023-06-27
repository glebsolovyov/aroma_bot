from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.keyboards import increase_the_tariff

next_care_button = InlineKeyboardButton('✅ Далее', callback_data='next_care')
mom_of_baby_keyboard = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, next_care_button)

about_me_button = InlineKeyboardButton('✅ О себе', callback_data='about_me')
about_baby_button = InlineKeyboardButton('✅ О малыше', callback_data='about_baby')

care_keyboard = InlineKeyboardMarkup(row_width=1).add(about_me_button, about_baby_button)

next_basic_rules_button = InlineKeyboardButton('✅ Далее', callback_data='next_basic_rules4')
next_basic_rules_keyboard = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, next_basic_rules_button)

next_actual_button = InlineKeyboardButton('✅ Далее', callback_data='actual')
next_actual_keyboard = InlineKeyboardMarkup(row_width=1).add(next_actual_button)

hemorrhoids = InlineKeyboardButton('✅ Восстановление промежности, геморрой', callback_data='hemorrhoids')
belly = InlineKeyboardButton('✅ Восстановление живота, работа с рубцом КС', callback_data='belly')
lactation = InlineKeyboardButton('✅ Налаживания лактации', callback_data='lactation')

actual_keyboard = InlineKeyboardMarkup(row_width=1).add(hemorrhoids, belly, lactation)