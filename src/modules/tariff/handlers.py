from aiogram import types, dispatcher, Dispatcher

from bot import bot
from messages import messages_tariffs

from . import keyboards


async def increase_the_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_tariffs.MESSAGE_FOR_BASE_TARIF,
                           reply_markup=keyboards.buy_base_tariff_keyboard)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_tariffs.MESSAGE_FOR_BASE_WITH_FEEDBACK_TARIFF,
                           reply_markup=keyboards.buy_base_with_feedback_tariff_keyboard)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_tariffs.MESSAGE_FOR_MENTORING_TARIF,
                           reply_markup=keyboards.buy_mentoring_tariff_keyboard)

    await callback_query.answer()


def register_all_tariff_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': increase_the_tariff, 'text': 'increase_the_tariff'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
