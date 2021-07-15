from django import forms

from books.models import BookModel


#
# class ContactForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     comment = forms.CharField(widget=forms.Textarea)


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        # fields = ['title', 'author', 'genres', 'cover', 'isbn', 'page_count', 'summary']
        exclude = ['created_at', 'cropping']
