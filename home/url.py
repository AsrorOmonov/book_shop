from django.urls import path

from home.views import IndexListView, BookDetailView

app_name = 'home'

urlpatterns = [
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('', IndexListView.as_view(), name='index'),
]
