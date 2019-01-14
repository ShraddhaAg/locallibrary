from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_visits = request.session.get('num_visits', 0)

    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    queryset = Book.objects.order_by('title')

class BookDetailView(generic.DetailView):
    model = Book
    template_name ='catalog/bookdetail.html'

class AuthorListView(generic.ListView):
     model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
