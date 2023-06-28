from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.keyboards import increase_the_tariff, want_butter

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

precautions_button = InlineKeyboardButton('✅ Далее', callback_data='precautions')
precautions_keyboard = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, precautions_button)

next_precautions_button = InlineKeyboardButton('✅ Далее', callback_data='next_precautions')
next_precautions_keyboard = InlineKeyboardMarkup(row_width=1).add(want_butter, next_precautions_button)

colic = InlineKeyboardButton('✅ Колики', callback_data='colic')
temperature = InlineKeyboardButton('✅ Температура', callback_data='temperature')
teething = InlineKeyboardButton('✅ Прорезывание зубов', callback_data='teething')
infectious_diseases = InlineKeyboardButton('✅ Детские инфекционные заболевания (ветрянка, розеола)',
                                           callback_data='infectious_diseases')

useful_keyboard = InlineKeyboardMarkup(row_width=1).add(colic, temperature, teething, infectious_diseases)

temperature_actions = InlineKeyboardButton('✅ Действия при температуре', callback_data='temperature')
temperature_keyboard = InlineKeyboardMarkup(row_width=1).add(temperature_actions)
