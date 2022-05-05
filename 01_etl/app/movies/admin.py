from django.contrib import admin

from movies.models import Filmwork, Genre, GenreFilmwork, Person, PersonFilmWork


class GenreFilmworkInline(admin.TabularInline):
    list_select_related = ['genre']
    model = GenreFilmwork
    extra = 0


class PersonFilmWorkInline(admin.TabularInline):
    list_select_related = ['person']
    model = PersonFilmWork
    extra = 0


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmWorkInline)
    list_display = ('title', 'type', 'creation_date', 'rating',)
    list_filter = ('type',)
    search_fields = ('title', 'description', 'id')
    list_per_page = 10

    def get_queryset(self, request):
        return super().get_queryset(request).with_related()


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'id')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'id')
