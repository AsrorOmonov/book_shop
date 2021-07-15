from modeltranslation.translator import register, TranslationOptions

from books.models import BookModel, GenreModel


@register(BookModel)
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'summary',)


@register(GenreModel)
class GenreTranslationOptions(TranslationOptions):
    fields = ('title',)
