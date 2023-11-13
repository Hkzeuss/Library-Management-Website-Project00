from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from category.models import Category
from book.models import Book
from author.models import Author
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from borrow.forms import Borrow
from django.contrib import messages
from datetime import datetime, timedelta


def tabrules(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }
    return render(request, 'student/tabrules.html', context)

def introduce(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
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
        # Truyền dữ liệu tìm kiếm vào template
        context = {
            
            'search_results': books,
            'search_book': search_book,
            'latest_categories': categories,
        }
    else:
        # Truyền dữ liệu danh mục vào template nếu không có tìm kiếm
        context = {
            'books': books,
            'latest_categories': categories,
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
        # Truyền dữ liệu tìm kiếm vào template
        context = {
            
            'search_results': books,
            'search_book': search_book,
            'latest_categories': categories,
        }
    else:
        context = {
            'category': category,
            'books': books,
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

    # Lấy thông tin chi tiết của thể loại của sách đã chọn
    category = selected_book.category

    # Lấy các sách cùng thể loại với sách đã chọn
    related_books = Book.objects.filter(category=category)

    categories = Category.objects.all()

    authors = Author.objects.all()

    print(categories)
    print(authors)
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
        form = Borrow(request.POST)
        if form.is_valid():
            borrow_instance = form.save(commit=False)
            borrow_instance.book = selected_book

            # Lấy dữ liệu từ form
            borrow_date = form.cleaned_data['borrow_date']
            return_date = form.cleaned_data['return_date']

            # Kiểm tra điều kiện ngày trả lớn hơn ngày mượn và không cách nhau quá 7 ngày
            if return_date <= borrow_date or return_date - borrow_date > timedelta(days=7):
                messages.error(request, 'Ngày trả không hợp lệ. Vui lòng kiểm tra lại.')
            else:
                selected_book.amount -= 1
                selected_book.save()
                borrow_instance.save()

                borrowed_books = request.session.get('borrowed_books', [])
                borrowed_books.append({
                    'author': str(selected_book.author),
                    'image': selected_book.img.url,
                    'book_title': selected_book.title,
                    'borrow_date': str(borrow_date),
                    'return_date': str(return_date),
                })
                request.session['borrowed_books'] = borrowed_books
                context['is_borrowed'] = True
                return redirect('book_detail', pk=pk)
            
    else:
        form = Borrow()

    context['form'] = form

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
        # Truyền dữ liệu tìm kiếm vào template
        context = {
            
            'search_results': books,
            'search_book': search_book,
            'latest_categories': categories,
        }

    else:
        context = {
            'latest_authors': authors,
            'author': author,
            'books': books,
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
    # Lấy tất cả các sách và các danh mục từ database
    authors = Author.objects.all()
    categories = Category.objects.all()

    search_author = request.GET.get('search', '')
    if search_author:
        # Tìm kiếm theo tiêu đề của tác giả
        authors = authors.filter(title__icontains=search_author)
        # Truyền dữ liệu tìm kiếm vào template
        context = {
            'search_results': authors,
            'search_author': search_author,
            'latest_authors': authors,
            'latest_categories': categories,
        }
    else:
        # Truyền dữ liệu danh mục vào template nếu không có tìm kiếm
        context = {
            'latest_authors': authors,
            'latest_categories': categories,
        }

    # Render template với dữ liệu đã lấy
    return render(request, 'book/author.html', context)