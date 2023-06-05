from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Text, StateFilter

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import FEEDBACK_BTNS, MODE_BTNS, PDF_MODES_BTNS
from keyboards.kb_tools import feedback_kb, choose_file_mode_kb

from aiogram.types import CallbackQuery

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from bot_fms import FMSModes

router: Router = Router()


@router.message(Command(commands='start'), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                        reply_markup=choose_file_mode_kb(1, **MODE_BTNS))


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='feedback'), StateFilter(default_state))
async def process_feedback_command(message: Message):
    await message.answer(text=LEXICON_RU['/feedback'],
                        reply_markup=feedback_kb(1, **FEEDBACK_BTNS))


@router.callback_query(Text(text='pdf_mode'), StateFilter(default_state))
async def activate_pdf_mode(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(FMSModes.pdf_start)
    await callback.message.answer(text=LEXICON_RU['start_pdf_mode'],
                                reply_markup=choose_file_mode_kb(1, **PDF_MODES_BTNS))
    await callback.answer()


@router.callback_query(StateFilter(FMSModes.pdf_start), Text(text=PDF_MODES_BTNS.values()))
async def show_pdf_commands(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Запустил PDF режим')
    await callback.answer()


# @router.callback_query(Text(text='last_btn'))
# async def process_buttons_callback(callback: CallbackQuery):
    
#     await callback.message.edit_text(text=LEXICON_RU['/help'])
#     await callback.answer()
