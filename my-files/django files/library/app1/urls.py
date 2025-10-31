from django.urls import path
from . import views # import your views fromthe same app


urlpatterns = [
    path('home/', views.home, name='home'),
    path('book-list/', views.show_books, name='show_books'),
    path('delete-book/<int:pk>', views.delete_book, name='delete_book'),
    path('update-book/<int:pk>', views.update_book, name='update_book'),
    path('soft-delete-book/<int:pk>', views.soft_delete_book, name='soft_delete_book'),
]