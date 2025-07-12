# DELETE
# Delete the book titled "Nineteen Eighty-Four" and confirm the deletion
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()
print(books)

# Expected Output:
# The book should be removed from the database.
# The printed result should be an empty QuerySet: <QuerySet []>
