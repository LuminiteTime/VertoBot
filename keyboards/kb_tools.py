from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


def _create_url_inline_btn(text: str, url_input: str):
    return InlineKeyboardButton(text=LEXICON_RU[text] if text in LEXICON_RU else text,
                                url=url_input)


def feedback_kb(width: int, **btns: str):
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for text, data in btns.items():
        buttons.append(_create_url_inline_btn(data['text'], data['url']))
    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()


def choose_file_mode_kb(width: int, **btns: str):
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for text, data in btns.items():
        buttons.append(InlineKeyboardButton(
                            text=text,
                            callback_data=data))
    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()
