from aiogram import Bot, Dispatcher, types, executor

import config
from messages import start_messages

from modules import register_all_handlers
from keyboards import command_start_keyboard

bot = Bot(token=config.TELEGRAM_API_KEY)
dp = Dispatcher(bot)


async def __on_start_up(dispathcer: Dispatcher) -> None:
    register_all_handlers(dispathcer)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, start_messages.MESSAGE_FOR_COMMAND_START)
    await bot.send_message(message.chat.id, start_messages.MESSAGE_FOR_START_KEYBOARD,
                           reply_markup=command_start_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)