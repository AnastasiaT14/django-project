from django.shortcuts import render
from .models import Book

def Book_list(request):
    books = Book.objects.all()
    return render(request, 'book.html',  {'books': books})