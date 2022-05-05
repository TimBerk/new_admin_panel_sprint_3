import datetime
from enum import Enum
from typing import List, Optional, Set

from pydantic import BaseModel
from pydantic.fields import Field


class PersonFilmRole(Enum):
    ACTOR = 'actor'
    SOUND_DIRECTOR = 'sound_director'
    DIRECTOR = 'director'
    MUSIC_EDITOR = 'music_director'
    WRITER = 'writer'


class Person(BaseModel):
    id: str
    name: str = Field(alias='full_name')


class PersonFilmWork(Person):
    role_str: Optional[str] = Field(alias='role')
    film_work_id: Optional[str]


class PersonElastic(Person):
    name: str
    role: Set[str] = set()
    film_ids: Set[str] = set()


class Genre(BaseModel):
    id: str
    name: str


class GenreFilmwork(Genre):
    description: Optional[str]
    film_work_id: str


class GenreElastic(Genre):
    description: Optional[str]
    film_ids: Set[str] = set()


class Filmwork(BaseModel):
    id: str = Field(alias='fw_id')
    title: str
    description: Optional[str]
    rating: Optional[float]
    type: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    role: Optional[str]
    person_id: Optional[str] = Field(alias='id')
    person_name: Optional[str] = Field(alias='full_name')
    genre_id: Optional[str] = Field(alias='genre_id')
    genre_name: Optional[str] = Field(alias='name')


class FilmworkElastick(BaseModel):
    id: str
    title: str
    description: Optional[str]
    imdb_rating: Optional[float] = Field(alias='rating', default=0)
    genre: Set = set()
    director: List[Person] = []
    actors: List[Person] = []
    actors_names: Set = set()
    writers: List[Person] = []
    writers_names: Set = set()
