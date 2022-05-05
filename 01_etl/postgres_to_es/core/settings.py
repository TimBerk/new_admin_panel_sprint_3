import datetime
import logging
from pathlib import Path

import environ

from core.constants import GENRES_SETTINGS, MOVIES_SETTINGS, PERSONS_SETTINGS


BLOCK_SIZE = 100
TIME_TO_RESTART = 60
DEFAULT_DATE = datetime.datetime(year=2020, month=1, day=1)
FORMAT_DATE = '%Y-%m-%d %H:%M:%S'

env = environ.Env()
environ.Env.read_env(Path('./.env'))
logging.basicConfig(
    filename='loader.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

POSTGRES_DSL = {
    'dbname': env.str('POSTGRES_DB'),
    'user': env.str('POSTGRES_USER'),
    'password': env.str('POSTGRES_PASSWORD'),
    'host': env.str('DB_HOST', 'localhost'),
    'port': env.int('DB_PORT', 5435),
    'options': '-c search_path=content'
}

REDIS_DSL = {
    'host': env.str('REDIS_HOST', 'localhost'),
    'port': env.int('REDIS_PORT', 6379)
}

ELASTIC_DSL = {
    'hosts': [
        f'http://{env.str("ELASTIC_HOST", "localhost")}:'
        f'{env.int("ELASTIC_PORT", 9200)}'
    ],
    'basic_auth': (
        env.str('ELASTIC_USER'),
        env.str('ELASTIC_PASSWORD')
    )
}

ELASTIC_INDEX = {
    'movies': MOVIES_SETTINGS,
    'persons': PERSONS_SETTINGS,
    'genres': GENRES_SETTINGS
}
