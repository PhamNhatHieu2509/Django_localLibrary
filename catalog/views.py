from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Genre, Author
from django.views import generic
def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    def view_listBook():
        book_list = Book.objects.all()
        context = {
            'book_list': book_list,
        }
        return context