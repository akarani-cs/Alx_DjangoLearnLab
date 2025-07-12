# CREATE
# Create a Book instance with title "1984", author "George Orwell", and publication year 1949

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# A Book object should be successfully created and saved to the database.
# If printed: <Book: 1984>