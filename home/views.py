from django.views.generic import ListView, DetailView

from books.models import BookModel, GenreModel


class IndexListView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        get_data = self.request.GET
        books = BookModel.objects.order_by('-pk')

        q = get_data.get('q')
        if q:
            books = books.filter(title__icontains=q)

        genre = get_data.get('genre')
        if genre:
            books = books.filter(genres__id=genre)
        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = GenreModel.objects.all()
        return context


'''below is function based controller of Index hidden as "..."'''


# def index(request):
#     books = BookModel.objects.order_by('-pk')
#     q = request.GET.get('q')
#
#     if q:
#         books = books.filter(title__icontains=q)
#
#     genre = request.GET.get('genre')
#
#     if genre:
#         books = books.filter(genres__id=genre)
#
#     genres = GenreModel.objects.all()
#
#     context = {
#         'books': books,
#         'genres': genres
#     }
#
#     return render(request, 'index.html', context)

class BookDetailView(DetailView):
    template_name = 'detail.html'
    model = BookModel
