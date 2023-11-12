from django.shortcuts import render
from django.views.generic import ListView, DetailView
from borrow.models import Borrow


class BorrowListView(ListView):

    model = Borrow
    template_name = "borrow/home.html"
    context_object_name = 'borrowes'


class BorrowDetailView(DetailView):
    model = Borrow
    template_name = "borrow/borrow_detail.html"