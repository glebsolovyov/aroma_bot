from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot import bot, dp

from core.states import ButterState

from . import keyboards
from core.keyboards import keyboard_for_start, get_contact

from messages import messages_for_want_butter


async def want_butter(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_for_want_butter.MESSAGE_FOR_WANT_BUTTER,
                           reply_markup=keyboards.order_butter_keyboard)

    await callback_query.answer()


async def order_butter(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Введите свое имя:')

    await ButterState.name.set()


async def get_name(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Отправьте свой контакт:',
                           reply_markup=get_contact)

    await state.update_data(name=message.text)
    await ButterState.next()


def register_buy_butter_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': want_butter, 'text': 'want_butter'},
        {'callback': order_butter, 'text': 'order_butter'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)

    dispatcher.register_message_handler(callback=get_name, state=ButterState.name)
