from django.contrib import admin
from.models import Book
from Introduction_to_Django.LibraryProject.bookshelf.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year', 'book_age']
    
    # Configure list filters for enhanced filtering
    list_filter = [
        'author',
        'publication_year',
        'decade_filter', 
    ]
    
    search_fields = [
        'title',
        'author',
        'publication_year',
    ]
  
    ordering = ['title']
    
    # Fields to display in the detail form
    fields = ['title', 'author', 'publication_year']
    
    # Add list per page configuration
    list_per_page = 20
    
    # Custom method to display book age
    def book_age(self, obj):
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - obj.publication_year
        return f"{age} years"
    book_age.short_description = 'Book Age'
    
    # Custom filter for decades
    def decade_filter(self, obj):
        return f"{str(obj.publication_year)[:3]}0s"
    decade_filter.short_description = 'Decade'