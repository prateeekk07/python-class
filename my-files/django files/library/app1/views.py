from django.shortcuts import render ,  HttpResponse
from app1.models import Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, "home.html", {"prateek": books})

def show_books(request):
    pass

def update_book(request):
    pass

def delete_book(request):
    pass