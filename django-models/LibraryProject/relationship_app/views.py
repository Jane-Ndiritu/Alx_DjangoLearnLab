import django
from django.shortcuts import render
from django.views.generic.detail import DetailView 
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# --- Function-Based View: List all books ---
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# --- Class-Based View: Library details + books ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()
        return context
