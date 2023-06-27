from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.keyboards import increase_the_tariff

next_button = InlineKeyboardButton('✅ Далее', callback_data='basic_rules3')
third_trimester_keyboard = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, next_button)

next_states_button = InlineKeyboardButton('✅ Далее', callback_data='next_states')
next_states_keyboard = InlineKeyboardMarkup(row_width=1).add(next_states_button)

excess_weight_button = InlineKeyboardButton('✅ Растяжки и лишний вес', callback_data='excess_weight')
cystitis_button = InlineKeyboardButton('✅ Молочница, цистит', callback_data='cystitis')
insomnia_button = InlineKeyboardButton('✅ Бессонница, страх родов', callback_data='insomnia')
pressure_button = InlineKeyboardButton('✅ Давление', callback_data='pressure')
preparation_for_childbirth_button = InlineKeyboardButton('✅ Хочу подготовить промежности к родам.',
                                                         callback_data='preparation_for_childbirth')

states_keyboard = InlineKeyboardMarkup(row_width=1).add(excess_weight_button, cystitis_button, insomnia_button,
                                                        pressure_button, preparation_for_childbirth_button)
