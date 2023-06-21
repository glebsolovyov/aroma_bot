from aiogram import types, Dispatcher

from . import keyboards
from bot import bot

from messages import messages_second_trimester


async def second_trimester(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_second_trimester.MESSAGE_FOR_SECOND_TRIMESTER,
                           reply_markup=keyboards.basic_rules_keyboard)

    await callback_query.answer()


async def basic_rules2(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_second_trimester.MESSAGE_BASIC_RULES,
                           reply_markup=keyboards.next_basic_rules_keyboard)

    await callback_query.answer()


async def bothering(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_second_trimester.MESSAGE_FOR_BOTHERING,
                           reply_markup=keyboards.bothering_keyboard)

    await callback_query.answer()


async def edema(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_second_trimester.MESSAGE_FOR_EDEMA,
                           reply_markup=keyboards.edema_increase_the_tariff_keyboard)

    await callback_query.answer()


async def edema_increase_the_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_second_trimester.MESSAGE_FOR_EDEMA_INCREASE_THE_TARIFF)

    await callback_query.answer()


def register_second_trimester_handlers(dispatcher: Dispatcher) -> None:

    callback_query_handlers = [
        {'callback': second_trimester, 'text': 'second_trimester'},
        {'callback': basic_rules2, 'text': 'basic_rules2'},
        {'callback': bothering, 'text': 'bothering'},
        {'callback': edema, 'text': 'edema'},
        {'callback': edema_increase_the_tariff, 'text': 'edema_increase_the_tariff'}
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)

