from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from bot import bot

from . import keyboards
from core.keyboards import keyboard_for_recommendations

from messages import messages_first_trimester
from core.messages import MESSAGE_BASIC_RULES

async def first_trimester(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_first_trimester.MESSAGE_FOR_PREGANCY_FIRST_TRIMESTER,
                           reply_markup=keyboards.basic_rules_keyboard)

    await callback_query.answer()


async def basic_rules1(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=MESSAGE_BASIC_RULES,
                           reply_markup=keyboards.next_basic_rules_keyboard)

    await callback_query.answer()


async def next_basic_rules1(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_first_trimester.MESSAGE_FOR_NEXT_BASIC_RULES)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_first_trimester.MESSAGE_FOR_HELP_YOURSELF,
                           reply_markup=keyboards.help_yourself_keyboard)

    await callback_query.answer()


async def nausea_and_heartburn(callback_query: types.CallbackQuery):
    media = [
        InputMediaPhoto(open('media/first_trimester/Breatne.jpeg', 'rb')),
        InputMediaPhoto(open('media/first_trimester/Lasential Oil Supplement.jpeg', 'rb'))
    ]

    await bot.send_media_group(chat_id=callback_query.message.chat.id,
                               media=media)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_first_trimester.MESSAGE_FOR_NAUSEA_AND_HEARTBURN,
                           reply_markup=keyboard_for_recommendations)


async def menace(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/first_trimester/IMG_9432.webp', 'rb'),
                         caption=messages_first_trimester.MESSAGE_FOR_MENACE,
                         reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def headache(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/first_trimester/IMG_9433.jpeg', 'rb'),
                         caption=messages_first_trimester.MESSAGE_FOR_HEADACHE,
                         reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def emotional_imbalance(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/first_trimester/Lavender.jpeg', 'rb'),
                         caption=messages_first_trimester.MESSAGE_FOR_EMOTIONAL_IMBALANCE,
                         reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


def register_first_trimester_handlers(dispatcher: Dispatcher) -> None:
    callback_query_handlers = [
        {'callback': first_trimester, 'text': 'first_trimester'},
        {'callback': basic_rules1, 'text': 'basic_rules1'},
        {'callback': next_basic_rules1, 'text': 'next_basic_rules1'},
        {'callback': nausea_and_heartburn, 'text': 'nausea_and_heartburn'},
        {'callback': menace, 'text': 'menace'},
        {'callback': headache, 'text': 'headache'},
        {'callback': emotional_imbalance, 'text': 'emotional_imbalance'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
