from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

basic_rules_button = InlineKeyboardButton('✅ Основные правила использования эфирных масел.', callback_data='basic_rules1')
basic_rules_keyboard = InlineKeyboardMarkup(row_width=1).add(basic_rules_button)

next_basic_rules_button = InlineKeyboardButton('✅ Далее', callback_data='next_basic_rules1')
next_basic_rules_keyboard = InlineKeyboardMarkup(row_width=1).add(next_basic_rules_button)


nausea_and_heartburn_button = InlineKeyboardButton('✅ тошноте и изжоге', callback_data='nausea_and_heartburn')
menace_button = InlineKeyboardButton('✅ угрозе', callback_data='menace')
headache_button = InlineKeyboardButton('✅ головных болях', callback_data='headache')
emotional_imbalance_button = InlineKeyboardButton('✅ эмоциональном дисбалансе', callback_data='emotional_imbalance')

help_yourself_keyboard = InlineKeyboardMarkup(row_width=1).add(nausea_and_heartburn_button, menace_button,
                                                               headache_button, emotional_imbalance_button)

nausea_and_heartburn_increase_the_tariff_button = InlineKeyboardButton('✅ повысить тариф',
                                                                       callback_data='nausea_and_heartburn_increase_the_tariff')
nausea_and_heartburn_increase_the_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(nausea_and_heartburn_increase_the_tariff_button)

menace_increase_the_tariff_button = InlineKeyboardButton('✅ повысить тариф',
                                                         callback_data='menace_increase_the_tariff')
menace_increase_the_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(menace_increase_the_tariff_button)

headache_increase_the_tariff_button = InlineKeyboardButton('✅ повысить тариф',
                                                           callback_data='headache_increase_the_tariff')
headache_increase_the_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(headache_increase_the_tariff_button)

emotional_imbalance_increase_the_tariff_button = InlineKeyboardButton('✅ повысить тариф',
                                                                      callback_data='emotional_imbalance_increase_the_tariff')
emotional_imbalance_increase_the_tariff_keyboard = InlineKeyboardMarkup(row_width=1).add(emotional_imbalance_increase_the_tariff_button)