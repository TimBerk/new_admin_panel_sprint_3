# Generated by Django 3.2 on 2022-04-17 07:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('certificate', models.TextField(blank=True, null=True, verbose_name='Certificate')),
                ('file_path', models.TextField(blank=True, null=True, verbose_name='Путь к файлу')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Creation date')),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Rating')),
                ('type', models.CharField(choices=[('movie', 'Movie'), ('tv_show', 'TV show')], default='movie', max_length=30, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Film work',
                'verbose_name_plural': 'Film works',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255, verbose_name='Full name')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('actor', 'Actor'), ('sound_director', 'Sound director'), ('director', 'Director'), ('music_director', 'Music director')], default='actor', max_length=30, verbose_name='Role')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='Film work')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'Person in the film work',
                'verbose_name_plural': 'Persons in the film work',
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='Film')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Genre of the film work',
                'verbose_name_plural': 'Genres of the film work',
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'person', 'role'), name='unique_person_role_in_film_work'),
        ),
        migrations.AlterUniqueTogether(
            name='genrefilmwork',
            unique_together={('film_work', 'genre')},
        ),
    ]