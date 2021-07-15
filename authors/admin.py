from django.contrib import admin

from authors.models import AuthorModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
