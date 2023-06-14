from aiogram import Dispatcher


def register_all_handlers(dispatcher: Dispatcher) -> None:
    from first_trimester.handlers import register_first_trimester_handlers
    from second_trimester.handlers import register_second_trimester_handlers

    handlers = [
        register_first_trimester_handlers,
        register_second_trimester_handlers
    ]

    for handler in handlers:
        handler(dispatcher)
