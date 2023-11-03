from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Book
from category.models import Category
# from student.models import CustomUser

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = 'books'


class HomeListView(ListView):

    model = Book
    template_name = "book/home.html"
    context_object_name = 'books'

    def get_context_data(self,  **kwargs):
        # student = self.request.user
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[
            :5]
        # context['students'] = CustomUser.objects.all()[:5]
        # context['student1'] = student
        # print(student.books)
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book_detail.html"


class BorrowBtn(LoginRequiredMixin, View):
    template_name = 'book/home.html'

    def post(self, request,  * args, **kwargs):

        book = get_object_or_404(Book, pk=kwargs['pk'])
        book.return_date = request.POST["return_date"]
        book.status = 'Borrowed'
        # std_pk = int(request.user.id)get_object_or_404(CustomUser, pk=std_pk)
        custom_user = request.user
        book.student = custom_user
        book.save()
        return redirect('book:book_detail', kwargs['pk'])

    def get(self, request, *args, **kwargs):

        return redirect('book:book')


class ReturnBtn(LoginRequiredMixin, View):

    def post(self, request,  * args, **kwargs):

        book = get_object_or_404(Book, pk=kwargs['pk'])
        book.return_date = None
        book.status = 'Available'
        book.student = None
        book.save()
        return redirect('book:book_detail', kwargs['pk'])

    def get(self, request, *args, **kwargs):

        return redirect('book:book')


class Search(View):

    def post(self, request,  * args, **kwargs):
        searchname = request.POST["search"]
        if searchname == '':
            return redirect('book:book')
        books = Book.objects.filter(title__startswith=searchname)
        books = books | Book.objects.filter(author__startswith=searchname)
        students = []
        # if request.user.is_staff:
        #     # students = CustomUser.objects.filter(
        #         # first_name__startswith=searchname)
        # return render(request, 'book/search.html', {'students': students, 'books': books})

    def get(self, request, *args, **kwargs):

        return redirect('book:book')
    

def tabrules(request):
    return render(request, 'student/tabrules.html')

def bookcase(request):
    return render(request, 'book/bookcase.html')

# Lịch sử
def hitstory(request):
    return render(request, "book/hitstory.html")

def hitstory_6(request):
    return render(request, "book/hitstory_6.html")

def hitstory_7(request):
    return render(request, "book/hitstory_7.html")

def hitstory_8(request):
    return render(request, "book/hitstory_8.html")

def hitstory_9(request):
    return render(request, "book/hitstory_9.html")

# Địa lý
def geography(request):
    return render(request, "book/geography.html")

def geography_6(request):
    return render(request, "book/geography_6.html")

def geography_7(request):
    return render(request, "book/geography_7.html")

def geography_8(request):
    return render(request, "book/geography_8.html")

def geography_9(request):
    return render(request, "book/geography_9.html")

# Giáo dục công dân
def education(request):
    return render(request, "book/education.html")

def education_6(request):
    return render(request, "book/education_6.html")

def education_7(request):
    return render(request, "book/education_7.html")

def education_8(request):
    return render(request, "book/education_8.html")

def education_9(request):
    return render(request, "book/education_9.html")

#Tiếng anh
def english(request):
    return render(request, "book/english.html")

def english_6(request):
    return render(request, "book/english_6.html")

def english_7(request):
    return render(request, "book/english_7.html")

def english_8(request):
    return render(request, "book/english_8.html")

def english_9(request):
    return render(request, "book/english_9.html")