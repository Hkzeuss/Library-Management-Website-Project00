from django.shortcuts import render

# Create your views here.
































































































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