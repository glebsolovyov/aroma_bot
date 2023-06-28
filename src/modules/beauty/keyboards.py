from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.keyboards import increase_the_tariff

next_beauty_button = InlineKeyboardButton('✅ Далее', callback_data='next_beauty')
next_beauty_keyboard = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, next_beauty_button)

face = InlineKeyboardButton('✅ Уделить внимание лицу', callback_data='face')
hair = InlineKeyboardButton('✅ Красота волос ', callback_data='hair')
deodorant = InlineKeyboardButton('✅ Дезодоранты и запах тела', callback_data='deodorant')
for_myself_keyboard = InlineKeyboardMarkup(row_width=1).add(face, hair, deodorant)

next_face_button = InlineKeyboardButton('✅ Далее', callback_data='next_face')
next_face_keyboard = InlineKeyboardMarkup(row_width=1).add(next_face_button)

next_skin_types_button = InlineKeyboardButton('✅ Далее', callback_data='next_skin_types')
next_skin_types_keyboard = InlineKeyboardMarkup(row_width=1).add(increase_the_tariff, next_skin_types_button)

normal = InlineKeyboardButton('✅ У меня нормальная кожа', callback_data='normal')
dry = InlineKeyboardButton('✅ У меня сухая кожа', callback_data='dry')
oily = InlineKeyboardButton('✅ У меня жирная кожа', callback_data='oily')
combination = InlineKeyboardButton('✅ У меня комбинированная кожа', callback_data='combination')
prone_to_allergy = InlineKeyboardButton('✅ У меня кожа, склонная к аллергии', callback_data='prone_to_allergy')
skin_types_keyboard = InlineKeyboardMarkup(row_width=1).add(normal, dry, oily, combination, prone_to_allergy)

serum = InlineKeyboardButton('✅ Сыворотка от выпадения волос', callback_data='serum')
conditioner = InlineKeyboardButton('✅ Кондиционер перед мытьем волос', callback_data='conditioner')
rinser = InlineKeyboardButton('✅ Ополаскиватель', callback_data='rinser')
shampoo = InlineKeyboardButton('✅ Шампунь', callback_data='shampoo')
for_hair_keyboard = InlineKeyboardMarkup(row_width=1).add(serum, conditioner, rinser, shampoo)
