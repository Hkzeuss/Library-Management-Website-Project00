from django.shortcuts import render
# , CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
#from .models import Book
from author.models import Author
# Create your views here.


class AuthorListView(ListView):

    model = Author
    template_name = "author/home.html"
    context_object_name = 'authores'


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author/author_detail.html"