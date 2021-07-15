from django.db import models
from django.utils.translation import ugettext_lazy as _


class AuthorModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    birth_date = models.IntegerField(null=True, verbose_name=_('birth_date'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
