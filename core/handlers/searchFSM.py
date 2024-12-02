from aiogram import Router, F
from aiogram.types import Message
from database import DBManeger
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

searchrouter = Router()
db_maneger = DBManeger('movies.db')

class SearchInfo(StatesGroup):
    film_code = State()

@searchrouter.message(F.text == 'Поиск🔍')
async def get_code(message: Message, state: FSMContext):
    await state.set_state(SearchInfo.film_code)
    await message.answer('Введите код фильма')

@searchrouter.message(SearchInfo.film_code)
async def search_film(message: Message, state: FSMContext):
    await state.update_data(film_code=message.text)
    data = await state.get_data()
    try:
        film_id = data['film_code']
        name, link = db_maneger.search_film(film_id)
        if name and link:
            await message.answer(f'Название: {name}\nСсылка: {link}')
        else:
            await message.answer('Фильм с таким кодом не найден')
    except:
        await message.answer('Фильм с таким кодом не найден')
    
    await state.clear()