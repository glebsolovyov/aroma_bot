from aiogram import types, Dispatcher

from bot import bot

from . import keyboards
from core.keyboards import keyboard_for_butters_and_start, keyboard_for_start

from messages import messages_beauty


async def beauty(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_BEAUTY,
                           reply_markup=keyboards.next_beauty_keyboard)

    await callback_query.answer()


async def next_beauty(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_NEXT_BEAUTY,
                           reply_markup=keyboards.for_myself_keyboard)

    await callback_query.answer()


async def face(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_FACE,
                           reply_markup=keyboards.next_face_keyboard)

    await callback_query.answer()


async def next_face(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_NEXT_FACE,
                           reply_markup=keyboards.next_skin_types_keyboard)

    await callback_query.answer()


async def next_skin_types(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_SKIN_TYPES,
                           reply_markup=keyboards.skin_types_keyboard)

    await callback_query.answer()


async def normal(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_NORMAL,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def dry(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_DRY,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def oily(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_OILY,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def combination(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_COMBINATION,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def hair(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_HAIR,
                           reply_markup=keyboards.for_hair_keyboard)

    await callback_query.answer()


async def serum(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_SERUM,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def conditioner(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_CONDITIONER,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def rinser(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_RINSER,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def shampoo(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_SHAMPOO,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def deodorant(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_beauty.MESSAGE_FOR_DEODARANT,
                           reply_markup=keyboard_for_butters_and_start)
def register_beauty_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': beauty, 'text': 'beauty'},
        {'callback': next_beauty, 'text': 'next_beauty'},
        {'callback': face, 'text': 'face'},
        {'callback': next_face, 'text': 'next_face'},
        {'callback': next_skin_types, 'text': 'next_skin_types'},
        {'callback': normal, 'text': 'normal'},
        {'callback': dry, 'text': 'dry'},
        {'callback': oily, 'text': 'oily'},
        {'callback': combination, 'text': 'combination'},
        {'callback': hair, 'text': 'hair'},
        {'callback': serum, 'text': 'serum'},
        {'callback': conditioner, 'text': 'conditioner'},
        {'callback': rinser, 'text': 'rinser'},
        {'callback': shampoo, 'text': 'shampoo'},
        {'callback': deodorant, 'text': 'deodorant'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
