from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

basic_rules_button = InlineKeyboardButton('✅ Основные правила использования эфирных масел.', callback_data='basic_rules1')
basic_rules_keyboard = InlineKeyboardMarkup(row_width=1).add(basic_rules_button)

next_basic_rules_button = InlineKeyboardButton('✅ Далее', callback_data='next_basic_rules1')
next_basic_rules_keyboard = InlineKeyboardMarkup(row_width=1).add(next_basic_rules_button)


nausea_and_heartburn_button = InlineKeyboardButton('✅ Тошноте и изжоге', callback_data='nausea_and_heartburn')
menace_button = InlineKeyboardButton('✅ Угрозе', callback_data='menace')
headache_button = InlineKeyboardButton('✅ Головных болях', callback_data='headache')
emotional_imbalance_button = InlineKeyboardButton('✅ Эмоциональном дисбалансе', callback_data='emotional_imbalance')

help_yourself_keyboard = InlineKeyboardMarkup(row_width=1).add(nausea_and_heartburn_button, menace_button,
                                                               headache_button, emotional_imbalance_button)

