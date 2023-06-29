from aiogram.dispatcher.filters.state import State, StatesGroup


class TariffState(StatesGroup):
    name = State()
    contact = State()


class ButterState(StatesGroup):
    name = State()
    contact = State()
