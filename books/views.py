from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from books.models import BookModel
from books.forms import BookModelForm


class BookListView(LoginRequiredMixin, ListView):
    """ data variable - object_list """
    template_name = 'my_admin/index.html'

    # model = BookModel
    # queryset = BookModel.objects.all()
    # context_object_name = 'book' --> if we want the name of object to be book (not mandatory)
    def get_queryset(self):
        q = self.request.GET.get('q')
        books = BookModel.objects.order_by('-pk')

        if q:
            books = books.filter(Q(title__icontains=q) | Q(author__name__icontains=q)).order_by('pk')
        else:
            books = BookModel.objects.all()
        return books


'''
 below function based controller hidden as "..."
'''


# def index(request):
#     q = request.GET.get('q')
#
#     if q:
#         books = BookModel.objects.filter(Q(title__icontains=q) | Q(author__name__icontains=q)).order_by('pk')
#     else:
#         books = BookModel.objects.all()
#
#     context = {
#         'books': books
#     }
#     return render(request, 'my_admin/index.html', context)


class BookDetailView(LoginRequiredMixin, DetailView):
    """ name of book object is - object """
    template_name = 'my_admin/detail.html'
    model = BookModel


'''
Function based view below hidden within "..."
'''


# def detail(request, pk):
#     # try:
#     #     book = BookModel.objects.get(pk=pk)
#     # except BookModel.DoesNotExist:
#     #     raise Http404
#
#     book = get_object_or_404(BookModel, pk=pk)
#     context = {
#         'book': book
#     }
#     return render(request, 'my_admin/detail.html', context) "" # 3"""

class BookCreateView(LoginRequiredMixin, CreateView):
    """ name of form variable is - object """
    template_name = 'my_admin/form.html'
    form_class = BookModelForm
    success_url = '/books/'  # redirect


def form_valid(self, form):
    body = f'{form.instance.title} is being added to database'
    send_mail(
        'Book is created',
        body,
        'Book management system administration',
        ['asroromonov230@gmail.com']
    )
    return super().form_valid(form)


''' 
    below is function based controller hidden as "..."
'''


# def create_book(request):
#     if request.method == 'POST':
#         form = BookModelForm(request.POST, files=request.FILES)
#         # files=request.FILES
#         if form.is_valid():
#             form.save()
#
#         return redirect('/books/create/')
#
#     else:
#
#         form = BookModelForm()
#
#         context = {
#             'form': form
#         }
#         return render(request, 'my_admin/form.html', context)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'my_admin/form.html'
    form_class = BookModelForm
    success_url = '/books/'
    model = BookModel


''' below function based controller hidden as "..." '''


# def edit_book(request, pk):
#     book = get_object_or_404(BookModel, pk=pk)
#
#     if request.method == 'POST':
#         form = BookModelForm(request.POST, files=request.FILES, instance=book)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect('/books/')
#
#     else:
#
#         form = BookModelForm(instance=book)
#
#         context = {
#             'form': form
#         }
#         return render(request, 'my_admin/form.html', context)

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = BookModel
    success_url = '/books/'


# def delete_book(request, pk):
#     book = get_object_or_404(BookModel, pk=pk)
#     book.delete()
#     return redirect('/books/')

# recursion multiplication
def multiply(a, b):
    counter = a
    if b == 0:
        return 0
    return counter + multiply(a, b - 1)


# recursion division
def divide(a, b):
    counter = 1
    if b < a:
        return 0
    return counter + divide(a - b, b)
