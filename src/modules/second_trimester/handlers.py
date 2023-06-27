from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from bot import bot

from . import keyboards
from core.keyboards import keyboard_for_recommendations

from messages import messages_second_trimester
from core.messages import MESSAGE_BASIC_RULES


async def second_trimester(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_second_trimester.MESSAGE_FOR_SECOND_TRIMESTER,
                           reply_markup=keyboards.basic_rules_keyboard)

    await callback_query.answer()


async def basic_rules2(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=MESSAGE_BASIC_RULES,
                           reply_markup=keyboards.next_basic_rules_keyboard)

    await callback_query.answer()


async def bothering(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_second_trimester.MESSAGE_FOR_BOTHERING,
                           reply_markup=keyboards.bothering_keyboard)

    await callback_query.answer()


async def edema(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/second_trimester/Lavender.jpeg', 'rb'),
                         caption=messages_second_trimester.MESSAGE_FOR_EDEMA,
                         reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def back_pain(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_second_trimester.MESSAGE_FOR_BACK_PAIN,
                           reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def constipation(callback_query: types.CallbackQuery):
    media = [
        InputMediaPhoto(open('media/second_trimester/IMG_9444.jpeg', 'rb')),
        InputMediaPhoto(open('media/second_trimester/Geranium.jpeg', 'rb'))
    ]
    await bot.send_media_group(chat_id=callback_query.message.chat.id,
                               media=media)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_second_trimester.MESSAGE_FOR_CONSTIPATION,
                           reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


def register_second_trimester_handlers(dispatcher: Dispatcher) -> None:
    callback_query_handlers = [
        {'callback': second_trimester, 'text': 'second_trimester'},
        {'callback': basic_rules2, 'text': 'basic_rules2'},
        {'callback': bothering, 'text': 'bothering'},
        {'callback': edema, 'text': 'edema'},
        {'callback': back_pain, 'text': 'back_pain'},
        {'callback': constipation, 'text': 'constipation'}
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
