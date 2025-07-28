# RETRIEVE
# Retrieve and display all attributes of the book titled "1984"
book = Book.objects.get(title="1984")
print(book.id, book.title, book.author, book.publication_year)

# Expected Output:
# Example: 1 1984 George Orwell 1949
# (Actual ID may vary depending on your database state)
