from django.db import models
from django.utils.translation import gettext as _


class FilmworkType(models.TextChoices):
    MOVIE = 'movie', _('Movie')
    TV_SHOW = 'tv_show', _('TV show')


class PersonFilmRole(models.TextChoices):
    ACTOR = 'actor', _('Actor')
    SOUND_DIRECTOR = 'sound_director', _('Sound director')
    DIRECTOR = 'director', _('Director')
    MUSIC_EDITOR = 'music_director', _('Music director')
    WRITER = 'writer', _('Writer')
