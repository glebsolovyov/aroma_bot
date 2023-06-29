from aiogram import types, dispatcher, Dispatcher

from bot import bot
from bot import dp
from messages import messages_tariffs

from . import keyboards


class Tariff:
    name = None


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


async def buy_base_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Введите номер телефона: ',
                           reply_markup=keyboards.get_contact)
    Tariff.name = 'Базовый'
    await callback_query.answer()


async def buy_base_with_feedback(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Введите номер телефона: ',
                           reply_markup=keyboards.get_contact)

    Tariff.name = 'Базовый с обратной связью'
    await callback_query.answer()


async def buy_mentoring_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Введите номер телефона: ',
                           reply_markup=keyboards.get_contact)

    Tariff.name = 'Наставничество'
    await callback_query.answer()


def register_all_tariff_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': increase_the_tariff, 'text': 'increase_the_tariff'},
        {'callback': buy_base_tariff, 'text': 'buy_base_tarif'},
        {'callback': buy_base_with_feedback, 'text': 'buy_base_with_feedback'},
        {'callback': buy_mentoring_tariff, 'text': 'buy_mentoring_tariff'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
