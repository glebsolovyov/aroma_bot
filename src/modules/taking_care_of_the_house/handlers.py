from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from bot import bot

from . import keyboards
from core.keyboards import keyboard_for_start

from messages import messages_taking_care_of_the_house


async def taking_care_of_the_house(callback_query: types.CallbackQuery):
    media = [
        InputMediaPhoto(open('media/taking_care_of_the_house/Lasential Oil Supplement.jpeg', 'rb'),
                        caption=messages_taking_care_of_the_house.MESSAGE_FOR_TAKING_CARE),
        InputMediaPhoto(open('media/taking_care_of_the_house/Lavender.jpeg', 'rb')),
        InputMediaPhoto(open('media/taking_care_of_the_house/IMG_9433.jpeg', 'rb')),
    ]

    await bot.send_media_group(chat_id=callback_query.message.chat.id, media=media)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text='Категории:',
                           reply_markup=keyboards.categories_keyboard)

    await callback_query.answer()


async def washing(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_taking_care_of_the_house.MESSAGE_FOR_WASHING,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def disinfection(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_taking_care_of_the_house.MESSAGE_FOR_DISINFECTION,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def stickers(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_taking_care_of_the_house.MESSAGE_FOR_STICKERS,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def appearance_of_things(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_taking_care_of_the_house.MESSAGE_FOR_APPEARANCE_OF_THINGS,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def unpleasant_odors(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_taking_care_of_the_house.MESSAGE_FOR_UNPLEASANT_ODORS,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def insects_house(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_taking_care_of_the_house.MESSAGE_FOR_INSECTS_HOUSE,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


def register_taking_care_of_the_house_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': taking_care_of_the_house, 'text': 'taking_care_of_the_house'},
        {'callback': washing, 'text': 'washing'},
        {'callback': disinfection, 'text': 'disinfection'},
        {'callback': stickers, 'text': 'stickers'},
        {'callback': appearance_of_things, 'text': 'appearance_of_things'},
        {'callback': unpleasant_odors, 'text': 'unpleasant_odors'},
        {'callback': insects_house, 'text': 'insects_house'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)