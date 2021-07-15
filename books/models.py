from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from image_cropping import ImageRatioField

from authors.models import AuthorModel
from books.validators import image_dimension_validator as _

from django.utils.translation import ugettext_lazy as _


class GenreModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')


class BookModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, related_name='books', verbose_name=_('author'))
    genres = models.ManyToManyField(GenreModel, related_name='books', verbose_name=_('genres'))
    cover = models.ImageField(upload_to='books', null=True, blank=True, verbose_name=_('cover'))
    cropping = ImageRatioField('cover', '100x100', free_crop=True, verbose_name=_('cropping'))
    isbn = models.CharField(max_length=13, unique=True, verbose_name=_('ISBN'))
    page_count = models.IntegerField(null=True, blank=True, verbose_name=_('page_count'))
    summary = RichTextUploadingField(verbose_name=_('summary'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')

# validators=[image_dimension_validator]
