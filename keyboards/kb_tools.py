from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


def _create_url_inline_btn(text: str, url_input: str):
    return InlineKeyboardButton(text=LEXICON_RU[text] if text in LEXICON_RU else text,
                                url=url_input)



def create_inline_kb(width: int,
                     *args: str,
                     last_btn: bool | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_RU[button] if button in LEXICON_RU else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            if type(text) == dict:
                buttons.append(_create_url_inline_btn(text['text'], text['url']))
            else:
                buttons.append(InlineKeyboardButton(
                    text=text,
                    callback_data=button))

    kb_builder.row(*buttons, width=width)

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
                            text=LEXICON_RU['last_btn'],
                            callback_data='last_btn'))

    return kb_builder.as_markup()

