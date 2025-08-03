# Import the serializers module from Django REST Framework.
from rest_framework import serializers

# Import the Book model from the current app's models module.
from .models import Book

# Define a serializer class for the Book model.
# It subclasses ModelSerializer which provides automatic field generation
# based on the Django model.
class BookSerializer(serializers.ModelSerializer):
    # Inner Meta class tells DRF which model to base this serializer on
    # and which fields to include.
    class Meta:
        model = Book          # The Django model to serialize/deserialize.
        fields = "__all__"    # Include all fields from the Book model.