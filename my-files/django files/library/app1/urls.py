from django.urls import path
from . import views # import your views fromthe same app


urlpatterns = [
    path('', views.home, name='home'),
]