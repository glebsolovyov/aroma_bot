from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot import bot, dp


from core.keyboards import keyboard_for_start, get_contact
from . import keyboards

from core.states import TariffState

from messages import messages_tariffs


class Tariff:
    tariff = None


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
                           text='Введите свое имя:')

    Tariff.tariff = 'Базовый'
    await TariffState.name.set()


async def buy_base_with_feedback(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Введите свое имя:')

    Tariff.tariff = 'Базовый с обратной связью'
    await TariffState.name.set()


async def buy_mentoring_tariff(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Введите свое имя:')

    Tariff.tariff = 'Наставничество'
    await TariffState.name.set()


async def get_name(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Отправьте свой контакт:',
                           reply_markup=get_contact)

    await state.update_data(name=message.text)
    await TariffState.next()


def register_all_tariff_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': increase_the_tariff, 'text': 'increase_the_tariff'},
        {'callback': buy_base_tariff, 'text': 'buy_base_tariff'},
        {'callback': buy_base_with_feedback, 'text': 'buy_base_with_feedback'},
        {'callback': buy_mentoring_tariff, 'text': 'buy_mentoring_tariff'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)

    dispatcher.register_message_handler(callback=get_name, state=TariffState.name)
