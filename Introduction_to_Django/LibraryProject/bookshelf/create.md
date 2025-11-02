from bookshelf.models import Book

# Create and save book instance in one step
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Verify creation
print(f"Book ID: {book.id}")
print(f"Book details: {book}")
