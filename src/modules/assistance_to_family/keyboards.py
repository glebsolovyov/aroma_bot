from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

prevention_of_infections = InlineKeyboardButton('✅ Профилактика орви, инфекций и т.д.',
                                                callback_data='prevention_of_infections')
temperature = InlineKeyboardButton('✅ Температура', callback_data='temperature')
otitis = InlineKeyboardButton('✅ Отиты', callback_data='otitis')
cough = InlineKeyboardButton('✅ Кашель', callback_data='cough')
rhinitis = InlineKeyboardButton('✅ Насморк', callback_data='rhinitis')
burns_cuts = InlineKeyboardButton('✅ Ожоги, порезы, травмы', callback_data='burns_cuts')
disorders = InlineKeyboardButton('✅ Расстройства ЖКТ', callback_data='disorders')
headache_assistance = InlineKeyboardButton('✅ Головная боль, боль в спине, ногах', callback_data='headache_assistance')
stress = InlineKeyboardButton('✅ Стресс, концентрация внимания', callback_data='stress')
allergies_fungus = InlineKeyboardButton('✅ Аллергии, грибок', callback_data='allergies_fungus')
insects = InlineKeyboardButton('✅ Насекомые', callback_data='insects')

prevention_keyboard = InlineKeyboardMarkup(row_width=1).add(prevention_of_infections, temperature, otitis, cough,
                                                            rhinitis, burns_cuts, disorders, headache_assistance, stress,
                                                            allergies_fungus, insects)