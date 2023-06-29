from aiogram import Bot, Dispatcher, types, executor

from bot import bot

from modules.start.keyboards import command_start_keyboard

from messages import start_messages


async def to_the_start(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=start_messages.MESSAGE_FOR_START_KEYBOARD,
                           reply_markup=command_start_keyboard)

    await callback_query.answer()


def register_start_handler(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(callback=to_the_start, text='to_the_start')
