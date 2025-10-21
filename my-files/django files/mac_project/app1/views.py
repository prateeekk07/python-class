from django.shortcuts import render, HttpResponse

# Create your views here.

def test_view(request):
    return HttpResponse("<h1>Hello .. Welcome to B14</h1>")