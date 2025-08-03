# api/urls.py
from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")
urlpatterns = [
        # Route for the BookList view (ListAPIView)
    path("books/", BookList.as_view(), name="book-list"),

     # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
# This file defines the URL patterns for the API, including the BookList view and the BookViewSet.
# The router automatically generates the necessary URLs for the BookViewSet, allowing for CRUD operations.