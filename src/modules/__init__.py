from aiogram import Dispatcher


def register_all_handlers(dispatcher: Dispatcher) -> None:
    from .start.handlers import register_start_handler
    from .first_trimester.handlers import register_first_trimester_handlers
    from .second_trimester.handlers import register_second_trimester_handlers
    from .third_trimester.handlers import register_third_trimester_handlers
    from .mom_of_baby.handlers import register_mom_of_baby_handlers
    from .assistance_to_family.handlers import register_assistance_to_family_handlers
    from .beauty.handlers import register_beauty_handlers
    from .taking_care_of_the_house.handlers import register_taking_care_of_the_house_handlers
    from .tariff.handlers import register_all_tariff_handlers

    handlers = [
        register_start_handler,
        register_first_trimester_handlers,
        register_second_trimester_handlers,
        register_third_trimester_handlers,
        register_mom_of_baby_handlers,
        register_assistance_to_family_handlers,
        register_beauty_handlers,
        register_taking_care_of_the_house_handlers,
        register_all_tariff_handlers
    ]

    for handler in handlers:
        handler(dispatcher)
