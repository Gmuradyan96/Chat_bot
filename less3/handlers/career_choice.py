from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard

router = Router()


available_prof_names = ["Developer", "WEb dev", "Qa"]
available_prof_grades = ["Junior", "Middle", "Senior"]



class ChoiceProfNames(StatesGroup):
    choice_prof_names = State()
    choice_prof_grades = State()




#handler for command /prof
@router.message(Command('prof'))
async def cmd_prof(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f"Choose the profession {name} ",
                    reply_markup=make_row_keyboard(available_prof_names))
    await state.set_state(ChoiceProfNames.choice_prof_names)


@router.message(ChoiceProfNames.choice_prof_names, F.text.in_(available_prof_names))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_prof=message.text.lower())
    await message.answer(f" Thanks, now chose your grade ",
                    reply_markup=make_row_keyboard(available_prof_grades))
    await state.set_state(ChoiceProfNames.choice_prof_grades)



@router.message(ChoiceProfNames.choice_prof_names)
async def prof_chosen_incorrectly(message: types.Message):
    await message.answer(f"I dont understand about what profession you talk ",
                     reply_markup=make_row_keyboard(available_prof_names))



@router.message(ChoiceProfNames.choice_prof_names, F.text.in_(available_prof_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f" You chose {message.text.lower()} your grade. Your profession , "
                         f"{user_data.get('chosen_prof')}", reply_markup=types.ReplyKeyboardRemove())

    await state.clear()



@router.message(ChoiceProfNames.choice_prof_grades)
async def prof_chosen_incorrectly(message: types.Message):
    await message.answer(f"I dont know that grade ", reply_markup=make_row_keyboard(available_prof_names))



