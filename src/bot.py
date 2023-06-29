from aiogram import Bot, Dispatcher, types, executor

import config

from modules.tariff import handlers
from modules import register_all_handlers

from keyboards import command_start_keyboard
from core.keyboards import keyboard_for_start

from messages import start_messages



bot = Bot(token=config.TELEGRAM_API_KEY)
dp = Dispatcher(bot)


async def __on_start_up(dispathcer: Dispatcher) -> None:
    register_all_handlers(dispathcer)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, start_messages.MESSAGE_FOR_COMMAND_START)
    await bot.send_message(message.chat.id, start_messages.MESSAGE_FOR_START_KEYBOARD,
                           reply_markup=command_start_keyboard)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_user_contact(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Ваши данные добавлены. Скоро с вами сважутся.',
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.chat.id,
                           text='Вернуться в главное меню',
                           reply_markup=keyboard_for_start)

    await bot.send_message(chat_id='-916487809', text=f'Ссылка: t.me/{message.from_user.username}\n'
                                                      f'Номер телефона: {message.contact.phone_number}\n'
                                                      f'Тариф: {handlers.Tariff.name}')


# async def process_event(event, dp: Dispatcher):
#     update = json.loads(event['body'])
#     Bot.set_current(dp.src)
#     update = types.Update.to_object(update)
#     await dp.process_update(update)
#
#
# async def handler(event, context):
#     await __on_start_up(dp)
#     await process_event(event, dp)
#     return {'statusCode': 200, 'body': 'ok'}

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
