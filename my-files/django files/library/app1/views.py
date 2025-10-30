from django.shortcuts import render , HttpResponse, redirect
from app1.models import Book

# Create your views here.

def home(request):
    if request.method == "POST":
        data = request.POST
        book_id = data.get("id")

        book_name = data.get("nm")
        book_qty = data.get("qty")
        book_price = data.get("prc")
        book_author = data.get("auth")
        if not book_id:
            Book.objects.create(name=book_name, qty=book_qty, price=book_price, author=book_author)
        else:
            book_obj = Book.objects.get(id=book_id)
            book_obj.name = book_name
            book_obj.qty = book_qty
            book_obj.price = book_price
            book_obj.author = book_author
            book_obj.save()
    

        return redirect("show_books")
    else:
        return render(request, "home.html")

def show_books(request):
    books = Book.objects.all()
    return render(request, "show_books.html", {"all_books": books})

def update_book(request,pk):
    return render(request,"home.html",{"single_book": Book.objects.get(id=pk)})
    

def delete_book(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("show_books")