from django.shortcuts import render ,  HttpResponse
from app1.models import Book

# Create your views here.

def home(request):
    if request.method == "POST":
        data = request.POST
        book_name = data.get("nm")
        book_qty = data.get("qty")
        book_price = data.get("prc")
        book_author = data.get("auth")
        Book.objects.create(name=book_name, qty=book_qty, price=book_price, author=book_author)
        return HttpResponse("Book added successfully!!")
    else:
        return render(request, "home.html")

def show_books(request):
    books = Book.objects.all()
    return render(request, "show_books.html", {"all_books": books})

def update_book(request):
    pass

def delete_book(request):
    pass