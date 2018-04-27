from django.shortcuts import render
from bike_management.models import Category, Book
# Create your views here.
def index(request):
    context = {
        'book_num':Book.objects.all(),
    }
    # import ipdb; ipdb.set_trace();
    return render(request,'index.html', context)

def cat (request,category_id):
    context = {
        'book_num':Book.objects.all().filter(category__id = category_id),
        'category': Category.objects.all()

    }
    return render (request,'horror.html', context)

# เรียก function HttpResponse() เพื่อ return HTML text กลับไปแสดงผลบนหน้าจอ
# def horror(request):
#     context = {
#         'book_num':Book.objects.all(),
#     }
#     # import ipdb; ipdb.set_trace();
#     return render(request,'horror.html', context)
#
# def romance(request):
#     context = {
#         'book_num':Book.objects.all(),
#     }
#     # import ipdb; ipdb.set_trace();
#     return render(request,'romance.html', context)
#
# def mystery(request):
#     context = {
#         'book_num':Book.objects.all(),
#     }
#     # import ipdb; ipdb.set_trace();
#     return render(request,'mystery.html', context)