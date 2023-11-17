from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from category.models import Category
from book.models import Book
from author.models import Author
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime, timedelta
from borrow.forms import BorrowForm
from borrow.models import Borrow
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone


def tabrules(request):
    categories = Category.objects.all()
    user_authenticated = request.user.is_authenticated
    print(categories)
    context = {
        'latest_categories': categories,
        'user_authenticated': user_authenticated,
    }
    return render(request, 'student/tabrules.html', context)

def introduce(request):
    user_authenticated = request.user.is_authenticated
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
        'user_authenticated': user_authenticated,
    }
    return render(request, "student/introduce.html", context)

def booklib(request):
    # Lấy tất cả các sách và các danh mục từ database
    books = Book.objects.all()
    categories = Category.objects.all()

    search_book = request.GET.get('search', '')
    if search_book:
        # Tìm kiếm theo tên sách hoặc tác giả
        books = books.filter(Q(title__icontains=search_book) | Q(author__title__icontains=search_book))
        paginator = Paginator(books, 28)
        page = request.GET.get('page')

        try:
            books_paginated = paginator.page(page)
        except PageNotAnInteger:
            # Nếu page không phải là số nguyên, trả về trang đầu tiên
            books_paginated = paginator.page(1)
        except EmptyPage:
            # Nếu page lớn hơn số lượng trang, trả về trang cuối cùng
            books_paginated = paginator.page(paginator.num_pages)
        # Truyền dữ liệu tìm kiếm vào template
        context = {
            'books': books_paginated,
            'search_results': books,
            'search_book': search_book,
            'latest_categories': categories,
            'latest_categorie': categories,
        }
    else:
        paginator = Paginator(categories, 5)
        page = request.GET.get('page')

        try:
            categories_paginated = paginator.page(page)
        except PageNotAnInteger:
            # Nếu page không phải là số nguyên, trả về trang đầu tiên
            categories_paginated = paginator.page(1)
        except EmptyPage:
            # Nếu page lớn hơn số lượng trang, trả về trang cuối cùng
            categories_paginated = paginator.page(paginator.num_pages)
        # Truyền dữ liệu danh mục vào template nếu không có tìm kiếm
        context = {
            'books': books,
            'latest_categories': categories_paginated,
            'latest_categorie': categories,
        }

    # Render template với dữ liệu đã lấy
    return render(request, 'book/home.html', context)

def category_detail(request, pk):
    # Lấy thông tin chi tiết của loại sách với primary key là pk
    category = get_object_or_404(Category, pk=pk)
    categories = Category.objects.all()

    books = Book.objects.filter(category=category)

    search_book = request.GET.get('search', '')
    if search_book:
        # Tìm kiếm theo tên sách hoặc tác giả
        books = books.filter(Q(title__icontains=search_book) | Q(author__title__icontains=search_book))
        paginator = Paginator(books, 28)
        page = request.GET.get('page')

        try:
            books_paginated = paginator.page(page)
        except PageNotAnInteger:
            # Nếu page không phải là số nguyên, trả về trang đầu tiên
            books_paginated = paginator.page(1)
        except EmptyPage:
            # Nếu page lớn hơn số lượng trang, trả về trang cuối cùng
            books_paginated = paginator.page(paginator.num_pages)
        # Truyền dữ liệu tìm kiếm vào template
        context = {
            'books': books_paginated,
            'search_results': books,
            'search_book': search_book,
            'latest_categories': categories,
        }
    else:
        # Phân trang cho sách
        paginator = Paginator(books, 28)
        page = request.GET.get('page')

        try:
            books_paginated = paginator.page(page)
        except PageNotAnInteger:
            # Nếu page không phải là số nguyên, trả về trang đầu tiên
            books_paginated = paginator.page(1)
        except EmptyPage:
            # Nếu page lớn hơn số lượng trang, trả về trang cuối cùng
            books_paginated = paginator.page(paginator.num_pages)

        context = {
            'category': category,
            'books': books_paginated,
            'latest_categories': categories,
        }

    return render(request, 'book/category_detail.html', context)

def book_detail(request, pk):
    # Lấy thông tin chi tiết của sách với primary key là pk
    selected_book = get_object_or_404(Book, pk=pk)
    related_author = selected_book.author
    user = request.user
    
    if selected_book.amount == 0:
        is_book_available = False
        messages.error(request, 'Sách đã hết. Không thể mượn.')
    else:
        is_book_available = True

    category = selected_book.category
    related_books = Book.objects.filter(category=category)
    categories = Category.objects.all()
    authors = Author.objects.all()
    pdf_url = selected_book.pdf.url

 
    context = {
        'selected_book': selected_book,
        'related_books': related_books,
        'latest_categories': categories,
        'latest_authors': authors,
        'related_author': related_author,
        'is_book_available': is_book_available,
        'pdf_url': pdf_url,
        'is_borrowed': False,
    }

    if request.method == 'POST':
        if Borrow.objects.filter(user=request.user, book=selected_book).exists():
            messages.error(request, 'Bạn đã mượn sách này rồi.')
        else:
            form = BorrowForm(request.POST)
            if form.is_valid():
                borrow_instance = form.save(commit=False)
                borrow_instance.user = request.user
                borrow_instance.book = selected_book

                # Lấy dữ liệu từ form
                borrow_date = form.cleaned_data['borrow_date']
                return_date = form.cleaned_data['return_date']


                # Kiểm tra điều kiện ngày trả lớn hơn ngày mượn và không cách nhau quá 7 ngày
                if return_date <= borrow_date or return_date - borrow_date > timedelta(days=7) or borrow_date < timezone.now().date():
                    context['error_message'] = 'Ngày trả không hợp lệ. Vui lòng kiểm tra lại.'

                    selected_book.amount -= 1
                    selected_book.save()
                    borrow_instance.save()

                    borrowed_books = Borrow.objects.filter(user=request.user)
                    context['borrowed_books'] = borrowed_books
                    context['is_borrowed'] = True
                    context['error_message'] = None
                    return redirect('book_detail', pk=pk)
            
    else:
        form = BorrowForm()

    context['form'] = form
    context['is_book_borrowed'] = Borrow.objects.filter(user=request.user, book=selected_book).exists()

    return render(request, 'book/book_detail.html', context)

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    authors = Author.objects.all()
    books = Book.objects.filter(author=author)
    categories = Category.objects.all()

    search_book = request.GET.get('search', '')
    if search_book:
        # Tìm kiếm theo tên sách hoặc tác giả
        books = books.filter(Q(title__icontains=search_book) | Q(author__title__icontains=search_book))
        paginator = Paginator(books, 28)
        page = request.GET.get('page')

        try:
            books_paginated = paginator.page(page)
        except PageNotAnInteger:
            # Nếu page không phải là số nguyên, trả về trang đầu tiên
            books_paginated = paginator.page(1)
        except EmptyPage:
            # Nếu page lớn hơn số lượng trang, trả về trang cuối cùng
            books_paginated = paginator.page(paginator.num_pages)
        # Truyền dữ liệu tìm kiếm vào template
        context = {
            'books': books_paginated,
            'search_results': books,
            'search_book': search_book,
            'latest_categories': categories,
        }

    else:
        # Phân trang cho sách
        paginator = Paginator(books, 28)
        page = request.GET.get('page')

        try:
            books_paginated = paginator.page(page)
        except PageNotAnInteger:
            # Nếu page không phải là số nguyên, trả về trang đầu tiên
            books_paginated = paginator.page(1)
        except EmptyPage:
            # Nếu page lớn hơn số lượng trang, trả về trang cuối cùng
            books_paginated = paginator.page(paginator.num_pages)

        context = {
            'latest_authors': authors,
            'author': author,
            'books': books_paginated,
            'latest_authors': authors,
            'latest_categories': categories,
        }

    return render(request, 'book/author_detail.html', context)

def view_pdf(request, pk):
    # Lấy thông tin chi tiết của sách với primary key là pk
    selected_book = get_object_or_404(Book, pk=pk)

    # Lấy đường dẫn tới file PDF
    pdf_path = selected_book.pdf.path

    # Đọc file PDF
    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{selected_book.title}.pdf"'
        return response
    
def author(request):
    authors = Author.objects.all()
    categories = Category.objects.all()

    search_author = request.GET.get('search', '')
    if search_author:
        # Tìm kiếm theo tiêu đề của tác giả
        authors = authors.filter(Q(title__icontains=search_author))
        paginator = Paginator(authors, 60)
        page = request.GET.get('page')

        try:
            authors_paginated = paginator.page(page)
        except PageNotAnInteger:
            authors_paginated = paginator.page(1)
        except EmptyPage:
            authors_paginated = paginator.page(paginator.num_pages)
        # Truyền dữ liệu tìm kiếm vào template
        context = {

            'search_results': authors,
            'search_author': search_author,
            'latest_authors': authors_paginated,
            'latest_categories': categories,
        }
    else:
        paginator = Paginator(authors, 60)
        page = request.GET.get('page')

        try:
            authors_paginated = paginator.page(page)
        except PageNotAnInteger:
            authors_paginated = paginator.page(1)
        except EmptyPage:
            authors_paginated = paginator.page(paginator.num_pages)

        context = {
            'latest_authors': authors_paginated,
            'latest_categories': categories,
        }

    # Render template với dữ liệu đã lấy
    return render(request, 'book/author.html', context)