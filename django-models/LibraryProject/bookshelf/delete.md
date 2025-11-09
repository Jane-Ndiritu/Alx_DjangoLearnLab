from bookshelf.models import Book

book = Book.objects.create(title="Temp Book", author="Test Author", publication_year=2025)
book.delete() 

# Verify remaining books
remaining_books = Book.objects.all()
print(f"Remaining books: {list(remaining_books)}")
