from django.shortcuts import render, redirect
from bike_management.models import Category, Book
from .forms import addBook


# Create your views here.
def index(request):
    context = {
        'book_num': Book.objects.all(),
    }
    # import ipdb; ipdb.set_trace();
    return render(request, 'index.html', context)


def cat(request, category_id):
    context = {
        'book_num': Book.objects.all().filter(category__id=category_id),
        'category': Category.objects.all()

    }
    return render(request, 'horror.html', context)


def add_book(request):
    if request.method == "POST":
        form = addBook(request.POST, request.FILES)
        if form.is_valid():
            book_item = form.save()
            book_item.save()
            return redirect('add_book')
    else:
        form = addBook()
    return render(request, 'form.html', {'form': form})

# เรียก function HttpResponse() เพื่อ return HTML text กลับไปแสดงผลบนหน้าจอ
