from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from bot import bot

from . import keyboards
from core.keyboards import keyboard_for_recommendations, keyboard_for_butters_and_start, keyboard_for_start

from messages import messages_assistance_to_family


async def assistance_to_family(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_ASSISTANCE_TO_FAMILY)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_PREVENTION,
                           reply_markup=keyboards.prevention_keyboard)

    await callback_query.answer()


async def prevention_of_infections(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_PREVENTION_OF_INFECTIONS,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def temperature(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_TEMPERATURE,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def otitis(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_OTITIS,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def cough(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_COUGH,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def rhinitis(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_RHINITIS,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def burns_cuts(callbaclk_query: types.CallbackQuery):
    await bot.send_message(chat_id=callbaclk_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_BUTN_CUTS,
                           reply_markup=keyboard_for_start)

    await callbaclk_query.answer()


async def disorders(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_DISORDERS,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def headache_assistance(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_HEADACHE_ASSISTANCE,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def stress(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_STRESS,
                           reply_markup=keyboard_for_butters_and_start)

    await callback_query.answer()


async def allergies_fungus(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_ALLERGIES_FUNGUS,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


async def insects(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=messages_assistance_to_family.MESSAGE_FOR_INSECTS,
                           reply_markup=keyboard_for_start)

    await callback_query.answer()


def regiset_assistance_to_family_handlers(dispathcer: Dispatcher):
    callback_query_handlers = [
        {'callback': assistance_to_family, 'text': 'assistance_to_family'},
        {'callback': prevention_of_infections, 'text': 'prevention_of_infections'},
        {'callback': temperature, 'text': 'temperature'},
        {'callback': otitis, 'text': 'otitis'},
        {'callback': cough, 'text': 'cough'},
        {'callback': rhinitis, 'text': 'rhinitis'},
        {'callback': burns_cuts, 'text': 'burns_cuts'},
        {'callback': disorders, 'text': 'disorders'},
        {'callback': headache_assistance, 'text': 'headache_assistance'},
        {'callback': stress, 'text': 'stress'},
        {'callback': allergies_fungus, 'text': 'allergies_fungus'},
        {'callback': insects, 'text': 'insects'},
    ]

    for handler in callback_query_handlers:
        dispathcer.register_callback_query_handler(**handler)
