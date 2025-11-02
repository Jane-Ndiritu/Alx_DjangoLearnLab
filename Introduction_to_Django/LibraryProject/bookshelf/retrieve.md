from bookshelf.models import Book

book = Book.objects.get(title="1984")
attributes = {
    'id': book.id,
    'title': book.title,
    'author': book.author,
    'publication_year': book.publication_year
}

for key, value in attributes.items():
    print(f"{key.replace('_', ' ').title()}: {value}")