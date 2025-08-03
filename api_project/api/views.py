from django.shortcuts import render
from .models import Book
from  .serializers import BookSerializer
from rest_framework import generics 

class Booklist(generics.ListAPIView):
    queryset = Book.objects.all()  # Queryset to retrieve all Book objects
    serializer_class = BookSerializer  # Serializer to convert Book objects to JSON format          

    

# Create your views here.
