# UPDATE
# Update the title of "1984" to "Nineteen Eighty-Four" and save the changes
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# The book instance should be updated in the database.
# When retrieved again, book.title should return "Nineteen Eighty-Four"
