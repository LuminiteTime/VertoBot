from dataclasses import dataclass
from environs import Env
from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import LEXICON_COMMANDS_RU

@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None) -> Config:
    
    env: Env = Env()
    env.read_env()

    return Config(tg_bot=TgBot(token=env('TOKEN'),
                                admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                    db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')))


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command=command,
                                    description=description)
                                    for command, description in LEXICON_COMMANDS_RU.items()]
    await bot.set_my_commands(main_menu_commands)
