from django.urls import path

from books.views import BookListView, BookDetailView, BookUpdateView, BookDeleteView, BookCreateView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='delete'),
    path('create/', BookCreateView.as_view(), name='create'),
]
