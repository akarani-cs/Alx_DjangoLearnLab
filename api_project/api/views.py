from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Queryset to retrieve all Book objects
    serializer_class = BookSerializer  # Serializer to convert Book objects to JSON format          

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides all CRUD operations for Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer   
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow unauthenticated users to read, but require authentication for write operations
    
# Create your views here.
