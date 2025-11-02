from bookshelf.models import Book

# Create book instance
book = Book(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Explicitly save to database
book.save()

# Verify creation
print(f"Book ID: {book.id}")
print(f"Book details: {book}")