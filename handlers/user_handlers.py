from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Text
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import FEEDBACK_BUTTONS
from keyboards.kb_tools import create_inline_kb
from aiogram.types import CallbackQuery

router: Router = Router()


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='feedback'))
async def process_feedback_command(message: Message):
    kb = create_inline_kb(1, last_btn=True, **FEEDBACK_BUTTONS)
    await message.answer(text=LEXICON_RU['/feedback'],
                        reply_markup=kb)

@router.callback_query(Text(text='last_btn'))
async def process_buttons_callback(callback: CallbackQuery):
    
    await callback.message.edit_text(text=LEXICON_RU['/help'])
    await callback.answer()
