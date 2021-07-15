from django.contrib import admin
from image_cropping import ImageCroppingMixin
from modeltranslation.admin import TranslationAdmin

from books.models import GenreModel, BookModel


@admin.register(GenreModel)
class GenreModelAdmin(TranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BookModel)
class BookModelAdmin(ImageCroppingMixin, TranslationAdmin):
    list_display = ['title', 'author', 'isbn', 'page_count', 'created_at']
    list_filter = ['author', 'genres', 'created_at']
    search_fields = ['title', 'summary', 'isbn']
    autocomplete_fields = ['author', 'genres']

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
