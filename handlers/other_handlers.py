from aiogram import Router
from aiogram.types import Message
from aiogram import F
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message()
async def process_other_text_answers(message: Message):
   await message.answer(text=LEXICON_RU['other'])
