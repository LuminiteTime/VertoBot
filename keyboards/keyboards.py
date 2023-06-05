from lexicon.lexicon import LEXICON_RU

FEEDBACK_BTNS: dict[str, dict[str, str]] = {
    'me': {
            'text': LEXICON_RU['creator'],
            'url': 'tg://user?id=1062363884'
        },
    'botlink': {
            'text': LEXICON_RU['bot_name'],
            'url': 'tg://user?id=6185798537'
        }
}

MODE_BTNS: dict[str, str] = {
    'PDF': 'pdf_mode',
}

# Заменить на ссылки на LEXICON
PDF_MODES_BTNS: dict[str, str] = {
    LEXICON_RU['combine_pdf']: 'combine',
    LEXICON_RU['divide_pdf']: 'divide',
    LEXICON_RU['watermark_pdf']: 'watermark',
}
