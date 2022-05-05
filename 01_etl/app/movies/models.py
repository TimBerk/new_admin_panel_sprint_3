from django.contrib.postgres.aggregates import ArrayAgg
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from movies.enums import FilmworkType, PersonFilmRole
from movies.mixins import TimeStampedMixin, UUIDMixin


class FilmworkQuerySet(models.QuerySet):
    @staticmethod
    def _aggregate_person(role: PersonFilmRole):
        return ArrayAgg(
            'persons__full_name',
            filter=Q(personfilmwork__role=role),
            distinct=True
        )

    def with_related(self):
        return self.prefetch_related('genres', 'persons')

    def main_queryset(self):
        return self.with_related().annotate(
            actors=self._aggregate_person(PersonFilmRole.ACTOR),
            directors=self._aggregate_person(PersonFilmRole.DIRECTOR),
            writers=self._aggregate_person(PersonFilmRole.WRITER)
        ).order_by('title', 'creation_date')


class Filmwork(UUIDMixin, TimeStampedMixin):
    title = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)
    certificate = models.TextField(_('Certificate'), blank=True, null=True)
    file_path = models.TextField(_('File path'), blank=True, null=True)
    creation_date = models.DateTimeField(_('Creation date'), auto_now=True)
    rating = models.FloatField(
        _('Rating'),
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    type = models.CharField(
        _('Type'),
        max_length=30,
        choices=FilmworkType.choices,
        default=FilmworkType.MOVIE,
    )

    genres = models.ManyToManyField(
        'Genre', through='GenreFilmwork', verbose_name=_('Genres')
    )
    persons = models.ManyToManyField(
        'Person', through='PersonFilmWork', blank=True,
        verbose_name=_('Persons')
    )

    objects = FilmworkQuerySet.as_manager()

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('Film work')
        verbose_name_plural = _('Film works')
        ordering = ['title', 'creation_date']
        indexes = (
            models.Index(
                name="film_work_idx",
                fields=('title', 'creation_date', 'rating', 'type'),
            ),
        )

    def __str__(self):
        return self.title


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')
        ordering = ['name']
        indexes = (
            models.Index(
                name="genre_idx",
                fields=('name',)
            ),
        )

    def __str__(self):
        return self.name


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey(
        'Filmwork',
        verbose_name=_('Film'),
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        'Genre',
        verbose_name=_('Genre'),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = _('Genre of the film work')
        verbose_name_plural = _('Genres of the film work')
        unique_together = ['film_work', 'genre']
        indexes = (
            models.Index(
                name="genre_film_work_idx",
                fields=('genre_id', 'film_work_id')
            ),
        )

    def __str__(self):
        return f'{self.film_work.title}: {self.genre.name}'


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('Full name'), max_length=255)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        ordering = ['full_name']
        indexes = (
            models.Index(
                name="person_idx",
                fields=('full_name',)
            ),
        )

    def __str__(self):
        return self.full_name


class PersonFilmWork(UUIDMixin):
    film_work = models.ForeignKey(
        'Filmwork',
        on_delete=models.CASCADE,
        verbose_name=_('Film work')
    )
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        verbose_name=_('Person')
    )
    role = models.CharField(
        _('Role'),
        max_length=30,
        choices=PersonFilmRole.choices,
        default=PersonFilmRole.ACTOR,
    )
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('Person in the film work')
        verbose_name_plural = _('Persons in the film work')
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'person', 'role'],
                name='unique_person_role_in_film_work'
            )
        ]
        indexes = (
            models.Index(
                name="person_film_work_idx",
                fields=('person_id', 'film_work_id', 'role')
            ),
        )

    def __str__(self):
        return f'{self.film_work.title}: {self.person.full_name}({self.role})'
