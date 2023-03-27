from django import forms

from library_catalog.models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None, to_field_name='authr_name')

        fields = ('title', 'description', 'poster', 'author')

        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = ('first_name', 'last_name', 'bio', 'photo')

        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
