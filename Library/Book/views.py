from django.shortcuts import render, redirect
from Book.models import Book

# Create your views here.


# function based view(FBV)
def homepage(request):      # https request   / This is userdefined func
    all_books = Book.objects.all()
    # all_books = Book.active_objects.all()     # through Custom Manager
    # all_books = Book.active_objects.all().filter(is_deleted='N')
    # print(all_books)
    return render(request, template_name='home.html', context={"books": all_books})



def save_book(request):
    print("In save_book")
    b_name = request.POST.get("name")
    b_author = request.POST.get("auth")
    b_price = request.POST.get("price")
    b_qty = request.POST.get("qty")
    b_pub = request.POST.get("pub")   # 'pub': 'on'---
    print(b_name, b_author, b_price, b_qty, b_pub) 
    return redirect('welcome')


















