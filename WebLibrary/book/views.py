from django.shortcuts import render, get_object_or_404
from .models import Book
from category.models import Category
from book.models import Book
from author.models import Author
from django.db.models import Q


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

    # Lấy thông tin chi tiết của thể loại của sách đã chọn
    category = selected_book.category

    # Lấy các sách cùng thể loại với sách đã chọn
    related_books = Book.objects.filter(category=category)

    categories = Category.objects.all()

    authors = Author.objects.all()

    print(categories)
    print(authors)
          
    context = {
        'selected_book': selected_book,
        'related_books': related_books,
        'latest_categories': categories,
        'latest_authors': authors,
        'related_author': related_author,
    }

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
            'author': author,
            'books': books,
            'latest_authors': authors,
            'latest_categories': categories,
        }

    return render(request, 'book/author_detail.html', context)