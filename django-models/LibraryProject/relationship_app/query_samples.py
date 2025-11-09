#!/usr/bin/env python
"""
Relationship Query Samples Script
This script demonstrates various relationship queries for the library system.
"""

import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def setup_sample_data():
    """Create sample data for testing queries"""
    print("Setting up sample data...")
    
    # Clear existing data
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()
    
    # Create authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")
    author3 = Author.objects.create(name="Agatha Christie")
    
    # Create books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author2)
    book4 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author2)
    book5 = Book.objects.create(title="Murder on the Orient Express", author=author3)
    book6 = Book.objects.create(title="And Then There Were None", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="City Central Library")
    library2 = Library.objects.create(name="University Library")
    
    # Add books to libraries
    library1.books.add(book1, book2, book3, book5)  # Mixed collection
    library2.books.add(book3, book4, book6)  # Focus on fantasy and mystery
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)
    
    print("Sample data created successfully!\n")
    return author1, author2, library1, library2

def query_all_books_by_specific_author(author_name):
    """
    Query 1: Get all books by a specific author
    Demonstrates ForeignKey reverse relationship using objects.filter(author=author)
    """
    print("=" * 60)
    print("QUERY 1: All books by a specific author")
    print("=" * 60)
    
    try:
        # Get the author object first
        author = Author.objects.get(name=author_name)
        
        # Method using objects.filter(author=author) - the required format
        print(f"\nMethod - Using objects.filter(author=author) (Books by {author_name}):")
        books = Book.objects.filter(author=author)
        for book in books:
            print(f"  - {book.title}")
            
        return books
        
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []

def query_all_books_by_specific_author_alternative(author_name):
    """
    Alternative version showing both methods for comparison
    """
    try:
        author = Author.objects.get(name=author_name)
        
        print(f"\nComparison for {author_name}:")
        
        # Method 1: Using objects.filter(author=author) - the required format
        print("1. Using Book.objects.filter(author=author):")
        books1 = Book.objects.filter(author=author)
        for book in books1:
            print(f"   - {book.title}")
        
        # Method 2: Using reverse relationship (for reference)
        print("\n2. Using author.books.all() (reverse relationship):")
        books2 = author.books.all()
        for book in books2:
            print(f"   - {book.title}")
            
        return books1
        
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []

def list_all_books_in_library(library_name):
    """
    Query 2: List all books in a specific library
    Demonstrates ManyToManyField relationship
    """
    print("\n" + "=" * 60)
    print("QUERY 2: All books in a specific library")
    print("=" * 60)
    
    try:
        library = Library.objects.get(name=library_name)
        
        print(f"\nBooks in {library_name}:")
        books = library.books.all()
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
            
        return books
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return []

def retrieve_librarian_for_library(library_name):
    """
    Query 3: Retrieve the librarian for a specific library
    Demonstrates OneToOneField relationship using Librarian.objects.get(library=library)
    """
    print("\n" + "=" * 60)
    print("QUERY 3: Librarian for a specific library")
    print("=" * 60)
    
    try:
        library = Library.objects.get(name=library_name)
        
        # Method using Librarian.objects.get(library=library) - the required format
        print(f"\nMethod - Using Librarian.objects.get(library=library):")
        librarian = Librarian.objects.get(library=library)
        print(f"  Librarian: {librarian.name}")
        print(f"  Manages: {librarian.library.name}")
        
        return librarian
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for library '{library_name}'.")
        return None

def retrieve_librarian_alternative_methods(library_name):
    """
    Alternative methods to retrieve librarian showing different approaches
    """
    print("\n" + "=" * 60)
    print("ALTERNATIVE LIBRARIAN QUERY METHODS")
    print("=" * 60)
    
    try:
        library = Library.objects.get(name=library_name)
        
        print(f"\nComparison for {library_name}:")
        
        # Method 1: Using Librarian.objects.get(library=library) - required format
        print("1. Using Librarian.objects.get(library=library):")
        librarian1 = Librarian.objects.get(library=library)
        print(f"   - {librarian1.name}")
        
        # Method 2: Using reverse relationship (for reference)
        print("\n2. Using library.librarian (reverse relationship):")
        librarian2 = library.librarian
        print(f"   - {librarian2.name}")
        
        return librarian1
        
    except (Library.DoesNotExist, Librarian.DoesNotExist) as e:
        print(f"Error: {e}")
        return None

def additional_demonstration_queries():
    """Additional useful relationship queries"""
    print("\n" + "=" * 60)
    print("ADDITIONAL DEMONSTRATION QUERIES")
    print("=" * 60)
    
    # Query using objects.filter with author
    print("\n1. All books by J.K. Rowling using objects.filter:")
    try:
        rowling = Author.objects.get(name="J.K. Rowling")
        rowling_books = Book.objects.filter(author=rowling)
        for book in rowling_books:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print("  J.K. Rowling not found")
    
    # Query: Libraries that have books by a specific author using objects.filter
    print("\n2. Libraries with books by George Orwell (using objects.filter):")
    orwell_books = Book.objects.filter(author__name="George Orwell")
    libraries_with_orwell = Library.objects.filter(books__in=orwell_books).distinct()
    for library in libraries_with_orwell:
        print(f"  - {library.name}")

    # Query using Librarian.objects.get(library=...)
    print("\n3. Librarian for University Library using objects.get:")
    try:
        uni_library = Library.objects.get(name="University Library")
        uni_librarian = Librarian.objects.get(library=uni_library)
        print(f"  - {uni_librarian.name} manages {uni_librarian.library.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("  - Library or librarian not found")

def main():
    """Main function to run all query demonstrations"""
    print("RELATIONSHIP QUERY SAMPLES")
    print("=" * 60)
    
    # Setup sample data
    author1, author2, library1, library2 = setup_sample_data()
    
    # Run the required queries
    query_all_books_by_specific_author("George Orwell")
    query_all_books_by_specific_author_alternative("J.K. Rowling")
    list_all_books_in_library("City Central Library")
    retrieve_librarian_for_library("City Central Library")
    retrieve_librarian_alternative_methods("University Library")
    
    # Additional demonstrations
    additional_demonstration_queries()
    
    print("\n" + "=" * 60)
    print("ALL QUERIES COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()