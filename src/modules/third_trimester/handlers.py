from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from bot import bot

from . import keyboards
from core.keyboards import keyboard_for_recommendations, keyboard_for_butters_and_start

from messages import messages_third_trimester
from core.messages import MESSAGE_BASIC_RULES


async def third_trimester(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_third_trimester.MESSAGE_FOR_THIRD_TRIMESTER,
                           reply_markup=keyboards.third_trimester_keyboard)

    await callback_query.answer()


async def basic_rules3(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=MESSAGE_BASIC_RULES,
                           reply_markup=keyboards.next_states_keyboard)

    await callback_query.answer()


async def next_states(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_third_trimester.MESSAGE_FOR_STATES,
                           reply_markup=keyboards.states_keyboard)

    await callback_query.answer()


async def excess_weight(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_third_trimester.MESSAGE_FOR_EXCESS_WEIGHT,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def cystitis(callback_query: types.CallbackQuery):
    media = [
        InputMediaPhoto(open('media/third_trimester/dOTERRA.webp', 'rb')),
        InputMediaPhoto(open('media/third_trimester/IMG_9446.jpeg', 'rb'))
    ]

    await bot.send_media_group(chat_id=callback_query.message.chat.id, media=media)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_third_trimester.MESSAGE_FOR_CYSTITITS,
                           reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def insomnia(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/third_trimester/Frankincense.jpeg', 'rb'),
                         caption=messages_third_trimester.MESSAGE_FOR_INSOMNIA,
                         reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def pressure(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/third_trimester/IMG_9230.jpeg', 'rb'),
                         caption=messages_third_trimester.MESSAGE_FOR_PRESSURE,
                         reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def preparation_for_childbirth(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_third_trimester.MESSAGE_FOR_PREPARATION_FOR_CHILDBIRTH,
                           reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


def register_third_trimester_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': third_trimester, 'text': 'third_trimester'},
        {'callback': basic_rules3, 'text': 'basic_rules3'},
        {'callback': next_states, 'text': 'next_states'},
        {'callback': excess_weight, 'text': 'excess_weight'},
        {'callback': cystitis, 'text': 'cystitis'},
        {'callback': insomnia, 'text': 'insomnia'},
        {'callback': pressure, 'text': 'pressure'},
        {'callback': preparation_for_childbirth, 'text': 'preparation_for_childbirth'}
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
