from aiogram import types, Dispatcher

from . import keyboards
from bot import bot

from messages import messages_first_trimester


async def __first_trimester(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_PREGANCY_FIRST_TRIMESTER,
                           reply_markup=keyboards.basic_rules_keyboard)

    await callback_query.answer()


async def __basic_rules(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_BASIC_RULES,
                           reply_markup=keyboards.next_basic_rules_keyboard)

    await callback_query.answer()


async def __next_basic_rules(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_NEXT_BASIC_RULES)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=messages_first_trimester.MESSAGE_FOR_HELP_YOURSELF,
                           reply_markup=keyboards.help_yourself_keyboard)

    await callback_query.answer()


def register_first_trimester_handlers(dispatcher: Dispatcher) -> None:

    callback_query_handlers = [
        dict(callback=__first_trimester, text='first_trimester'),
        dict(callback=__basic_rules, text='basic_rules'),
        dict(callback=__next_basic_rules, text='next_basic_rules')
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
