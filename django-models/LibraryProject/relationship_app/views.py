from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# --- Function-Based View: List all books ---
def book_list(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"Title: {book.title} — Author: {book.author}\n"
    return HttpResponse(output, content_type="text/plain")


# --- Class-Based View: Library details + books ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()  # all books in this library
        return context
