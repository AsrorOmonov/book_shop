from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from books.views import BookDetailView, BookCreateView, BookUpdateView, BookListView, BookDeleteView
from home.views import IndexListView

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('books.url', 'books')),
    path('', include('home.url', 'home')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
