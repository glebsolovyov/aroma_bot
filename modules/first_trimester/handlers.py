from aiogram import types, Dispatcher

from . import keyboards
from bot import bot

from messages import messages_first_trimester


async def first_trimester(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_PREGANCY_FIRST_TRIMESTER,
                           reply_markup=keyboards.basic_rules_keyboard)

    await callback_query.answer()


async def basic_rules(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_BASIC_RULES,
                           reply_markup=keyboards.next_basic_rules_keyboard)

    await callback_query.answer()


async def next_basic_rules(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_NEXT_BASIC_RULES)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_HELP_YOURSELF,
                           reply_markup=keyboards.help_yourself_keyboard)

    await callback_query.answer()


async def nausea_and_heartburn(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_NAUSEA_AND_HEARTBURN,
                           reply_markup=keyboards.nausea_and_heartburn_increase_the_tariff_keyboard)

    await callback_query.answer()


async def nausea_and_heartburn_increase_the_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_NAUSEA_AND_HEARTBURN_INCREASE_THE_TARIFF)

    await callback_query.answer()


async def menace(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                            text=messages_first_trimester.MESSAGE_FOR_MENACE,
                            reply_markup=keyboards.menace_increase_the_tariff_keyboard)

    await callback_query.answer()


async def menace_increase_the_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_MENACE_INCREASE_THE_TARIFF)

    await callback_query.answer()


async def headache(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_HEADACHE,
                           reply_markup=keyboards.headache_increase_the_tariff_keyboard)

    await callback_query.answer()


async def headache_increase_the_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_HEADACHE_INCREASE_THE_TARIFF)

    await callback_query.answer()


async def emotional_imbalance(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_EMOTIONAL_IMBALANCE,
                           reply_markup=keyboards.emotional_imbalance_increase_the_tariff_keyboard)

    await callback_query.answer()


async def emotional_imbalance_increase_the_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_EMOTIONAL_IMBALANCE_INCREASE_THE_TARIFF)

    await callback_query.answer()


def register_first_trimester_handlers(dispatcher: Dispatcher) -> None:

    callback_query_handlers = [
        {'callback': first_trimester, 'text': 'first_trimester'},
        {'callback': basic_rules, 'text': 'basic_rules'},
        {'callback': next_basic_rules, 'text': 'next_basic_rules'},
        {'callback': nausea_and_heartburn, 'text': 'nausea_and_heartburn'},
        {'callback': nausea_and_heartburn_increase_the_tariff, 'text': 'nausea_and_heartburn_increase_the_tariff'},
        {'callback': menace, 'text': 'menace'},
        {'callback': menace_increase_the_tariff, 'text': 'menace_increase_the_tariff'},
        {'callback': headache, 'text': 'headache'},
        {'callback': headache_increase_the_tariff, 'text': 'headache_increase_the_tariff'},
        {'callback': emotional_imbalance, 'text': 'emotional_imbalance'},
        {'callback': emotional_imbalance_increase_the_tariff, 'text': 'emotional_imbalance_increase_the_tariff'}
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
