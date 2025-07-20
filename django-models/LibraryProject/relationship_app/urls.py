from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    CustomLoginView,
    CustomLogoutView,
)
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('', list_books, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Auth URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),

    
]


#"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="