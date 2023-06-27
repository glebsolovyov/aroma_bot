from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first_trimester = InlineKeyboardButton('✅ Беременность (первый триместр)', callback_data='first_trimester')
second_trimester = InlineKeyboardButton('✅ Беременность (второй триместр)', callback_data='second_trimester')
third_trimester = InlineKeyboardButton('✅ Беременность (третий триместр) и подготовка к родам',
                                       callback_data='third_trimester')

command_start_keyboard = InlineKeyboardMarkup(row_width=1).add(first_trimester, second_trimester, third_trimester)

