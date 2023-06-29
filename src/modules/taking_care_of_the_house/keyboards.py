from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

washing = InlineKeyboardButton('✅ Стирка', callback_data='washing')
disinfection = InlineKeyboardButton('✅ Дезинфекция поверхностей', callback_data='disinfection')
stickers = InlineKeyboardButton('✅ Трудно-выводимые вещества, наклейки', callback_data='stickers')
appearance_of_things = InlineKeyboardButton('✅ Внешний вид вещей', callback_data='appearance_of_things')
unpleasant_odors = InlineKeyboardButton('✅ Неприятные запахи', callback_data='unpleasant_odors')
insects_house = InlineKeyboardButton('✅ Насекомые', callback_data='insects_house')
categories_keyboard = InlineKeyboardMarkup(row_width=1).add(washing, disinfection, stickers, appearance_of_things,
                                                            unpleasant_odors, insects_house)
