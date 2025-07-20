from django.shortcuts import render
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView


def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    # Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registering
            return redirect('list_books')  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View (extends built-in view to use your template)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'



# Create your views here.
#relationship_app/list_books.html", "Book.objects.all()"
#["relationship_app/library_detail.html"