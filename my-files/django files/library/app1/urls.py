from django.urls import path
from . import views # import your views fromthe same app


urlpatterns = [
    path('home/', views.home, name='home'),
    path('book-list', views.show_books, name='show_books'),
]