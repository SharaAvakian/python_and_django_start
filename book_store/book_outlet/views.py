from django.db.models.aggregates import Avg
from django.shortcuts import render,get_object_or_404
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-id").reverse()
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))['rating__avg']
    return render(request,"book_outlet/index.html",{"books":books, "total_books":num_books,"average_rating":avg_rating})

def book_detail(request,slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{"title":book.title  , "author":book.author, "rating":book.rating, "is_bestseller":book.is_bestseller})
