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


kb = ReplyKeyboardMarkup()

button = KeyboardButton("Рассчитать")
button_2 = KeyboardButton("Информация")
button_3 = KeyboardButton("Купить")

kb.add(button, button_2, button_3)
kb.resize_keyboard = True


inline_kb = InlineKeyboardMarkup(row_width=4)
inline_button_1 = InlineKeyboardButton(text="Продукт 1", callback_data="product_buying")
inline_button_2 = InlineKeyboardButton(text="Продукт 2", callback_data="product_buying")
inline_button_3 = InlineKeyboardButton(text="Продукт 3", callback_data="product_buying")
inline_button_4 = InlineKeyboardButton(text="Продукт 4", callback_data="product_buying")
inline_kb.add(inline_button_1, inline_button_2, inline_button_3, inline_button_4)

@dp.message_handler(commands=["start"])
async def starter(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберете опцию:", reply_markup=kb)

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'files/{i}.jpg', 'rb') as img:
            await message.answer_photo(img, f"Название: Product{i} | Описание: описание {i} | Цена: {i * 100}")
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


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
 
