import json
import os

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import config

from modules.tariff import handlers
from modules import register_all_handlers

import keyboards
from core.keyboards import keyboard_for_start

from messages import start_messages

from core.states import TariffState, ButterState
from modules.tariff import handlers

bot = Bot(token=config.TELEGRAM_API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())


async def __on_start_up(dispathcer: Dispatcher) -> None:
    register_all_handlers(dispathcer)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, start_messages.MESSAGE_FOR_COMMAND_START,
                           reply_markup=keyboards.next_start_keyboard)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=TariffState.contact)
async def get_user_contact(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Ваши данные добавлены. Скоро с вами сважутся.',
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.chat.id,
                           text='Вернуться в главное меню',
                           reply_markup=keyboard_for_start)

    data = await state.get_data()
    await bot.send_message(chat_id='-916487809', text=f'Имя: {data.get("name")}\n'
                                                      f'Ссылка: t.me/{message.from_user.username}\n'
                                                      f'Номер телефона: {message.contact.phone_number}\n'
                                                      f'Тариф: {handlers.Tariff.tariff}')

    await state.finish()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=ButterState.contact)
async def get_user_contact(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Ваши данные добавлены. Скоро с вами сважутся.',
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.chat.id,
                           text='Вернуться в главное меню',
                           reply_markup=keyboard_for_start)

    data = await state.get_data()
    await bot.send_message(chat_id='-916487809', text=f'Имя: {data.get("name")}\n'
                                                      f'Ссылка: t.me/{message.from_user.username}\n'
                                                      f'Номер телефона: {message.contact.phone_number}\n'
                                                      f'Хочет заказать масла')

    await state.finish()

DEBUG = os.environ.get('DEBUG')
if DEBUG:
    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)

else:
    async def process_event(event, dp: Dispatcher):
        update = json.loads(event['body'])
        Bot.set_current(dp)
        update = types.Update.to_object(update)
        await dp.process_update(update)


    async def handler(event, context):
        await __on_start_up(dp)
        await process_event(event, dp)
        return {'statusCode': 200, 'body': 'ok'}
