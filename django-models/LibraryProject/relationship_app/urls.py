from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    CustomLoginView,
    CustomLogoutView,
)

urlpatterns = [
    path('', list_books, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Auth URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]


#"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="