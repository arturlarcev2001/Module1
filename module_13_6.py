from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

class UserState(StatesGroup):
    age, growth, weight = State(), State(), State()

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button_2 = InlineKeyboardButton(text="Формулы расчта", callback_data="formulas")
kb.add(button, button_2)


@dp.message_handler(commands=["start"])
async def starter(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберете опцию:", reply_markup=kb)

@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост.")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес.")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    perfect_calories = (10 * int(data["weight"])) + (6.25 * int(data["growth"])) - (5 * int(data["age"]) + 5)
    await message.answer(f"Вам необходимо потреблять {perfect_calories} каллорий в день")
    await state.finish()
    

@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите комманду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
 
