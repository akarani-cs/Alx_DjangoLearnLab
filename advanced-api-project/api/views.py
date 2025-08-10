from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
#"from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]




#ListView - Retrieve all Books

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #anyone can view

    #Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    # Step 2: Searching
    search_fields = ['title', 'author']

    # Step 3: Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering



#DetailView - Retrieve single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

#CreateView - Add a new book
class BookCreateView(CreateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #only logged-in users can create

    def perform_create(self, serializer):
        #Custom validation: publication year cannot be in the future
        pub_year = self.request.data.get('publication_year')
        current_year = timezone.now().year
        if pub_year and int(pub_year) > current_year:
            raise ValidationError({"publication_year": "Publication year cannot be in the future."})
        
        #Save the book with the current user as the creatpt (if applicable)
        serializer.save()



#Update abook with validation + custom permission

class BookUpdateView(generics.UpdateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [permissions.IsAuthenticated] #must be logged in

   def perform_update(self, serializer):
       pub_year = self.request.data.get('publication_year')
       current_year = timezone.now().year
       if pub_year and int(pub_year) > current_year:
           raise ValidationError({'publication_year':'Publication year cannot be in the future.' })
       serializer.save()
    

#DeleteView - Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
