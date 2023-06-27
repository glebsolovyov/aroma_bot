from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from bot import bot

from . import keyboards
from core.keyboards import keyboard_for_recommendations

from messages import messages_mom_of_baby
from core.messages import MESSAGE_BASIC_RULES


async def mom_of_baby(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_mom_of_baby.MESSAGE_FOR_MOM_OF_BABY,
                           reply_markup=keyboards.mom_of_baby_keyboard)

    await callback_query.answer()


async def next_care(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_mom_of_baby.MESSAGE_FOR_NEXT_CARE,
                           reply_markup=keyboards.care_keyboard)

    await callback_query.answer()


async def about_me(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_mom_of_baby.MESSAGE_FOR_ABOUT_ME,
                           reply_markup=keyboards.next_basic_rules_keyboard)

    await callback_query.answer()


async def next_basic_rules4(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=MESSAGE_BASIC_RULES,
                           reply_markup=keyboards.next_actual_keyboard)

    await callback_query.answer()


async def actual(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_mom_of_baby.MESSAGE_FOR_ACTUAL,
                           reply_markup=keyboards.actual_keyboard)

    await callback_query.answer()


async def hemorrhoids(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_mom_of_baby.MESSAGE_FOR_HEMORRHOIDS,
                           reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def belly(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_mom_of_baby.MESSAGE_FOR_BELLY,
                           reply_markup=keyboard_for_recommendations)

    await callback_query.answer()


async def lactation(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.message.chat.id,
                         photo=open('media/mom_of_baby/Fennel (sweet).jpeg', 'rb'),
                         caption=messages_mom_of_baby.MESSAGE_FOR_LACTATION,
                         reply_markup=keyboard_for_recommendations)

    await callback_query.answer()

def register_mom_of_baby_handlers(dispatcher: Dispatcher):
    callback_query_handlers = [
        {'callback': mom_of_baby, 'text': 'mom_of_baby'},
        {'callback': next_care, 'text': 'next_care'},
        {'callback': about_me, 'text': 'about_me'},
        {'callback': next_basic_rules4, 'text': 'next_basic_rules4'},
        {'callback': actual, 'text': 'actual'},
        {'callback': hemorrhoids, 'text': 'hemorrhoids'},
        {'callback': belly, 'text': 'belly'},
        {'callback': lactation, 'text': 'lactation'},
    ]

    for handler in callback_query_handlers:
        dispatcher.register_callback_query_handler(**handler)
