from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first_trimester = InlineKeyboardButton('✅ Беременность (первый триместр)', callback_data='first_trimester')

command_start_keyboard = InlineKeyboardMarkup(row_width=1).add(first_trimester)
