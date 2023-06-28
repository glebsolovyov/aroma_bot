from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first_trimester = InlineKeyboardButton('✅ Беременность (первый триместр)', callback_data='first_trimester')
second_trimester = InlineKeyboardButton('✅ Беременность (второй триместр)', callback_data='second_trimester')
third_trimester = InlineKeyboardButton('✅ Беременность (третий триместр) и подготовка к родам',
                                       callback_data='third_trimester')
mom_of_baby = InlineKeyboardButton('✅ Я мама малыша до 6 месяцев ', callback_data='mom_of_baby')
assistance_to_family = InlineKeyboardButton('✅ Помощь семье и старшим детям (старше 6 месяцев)',
                                            callback_data='assistance_to_family')
beauty = InlineKeyboardButton('✅ Красота после рождения детей', callback_data='beauty')

command_start_keyboard = InlineKeyboardMarkup(row_width=1).add(first_trimester, second_trimester, third_trimester,
                                                               mom_of_baby, assistance_to_family, beauty)

