from aiogram.fsm.state import StatesGroup, State


class BuyTariffState(StatesGroup):
    first_name = State()
    phone_number = State()
    email = State()

