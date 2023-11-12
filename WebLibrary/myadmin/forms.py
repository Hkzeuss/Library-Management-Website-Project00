from django import forms
from book.models import Book
from category.models import Category
from author.models import Author


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'description',  'img',
                  'category']
        try:
            categories = Category.objects.all()
        except:
            categories = list()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Title ',
                'id': 'title'}),
            'author': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Author ',
                'id': 'title'}),
            'description': forms.TextInput(attrs={
                'class': 'email text_box  ',
                'placeholder': 'Description ',
                'id': 'title'}),

            'img': forms.FileInput(attrs={
                'class': 'email text_box',
                'id': 'username'}),
            'category': forms.Select(choices=categories, attrs={'class': 'text_box  email', 'placeholder': 'Title '}),

        }
        labels = {
            'title': '',
            'author': '',
            'description': '',
            'category': '',
            'img': '',
        }

        def __init__(self, *args, **kwargs):
            super(CreateBookForm, self).__init__(*args, **kwargs)
            try:
                self.fields['category'].queryset = Category.objects.all()
            except:
                self.fields['category'].queryset = Category.objects.none()


class CreateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'img']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Title ',
                'id': 'title'}),

            'img': forms.FileInput(attrs={
                'class': 'email text_box',
                'id': 'username'}),

        }
        labels = {
            'title': '',
            'img': '',
        }

class CreateAuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['title', 'img']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Title ',
                'id': 'title'}),

            'img': forms.FileInput(attrs={
                'class': 'email text_box',
                'id': 'username'}),

        }
        labels = {
            'title': '',
            'img': '',
        }