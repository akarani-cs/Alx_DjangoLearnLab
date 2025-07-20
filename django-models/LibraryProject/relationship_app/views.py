from django.shortcuts import render
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test, login_required



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


def role_required(role):
    def check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(check)

@login_required
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



# Create your views here.
#relationship_app/list_books.html", "Book.objects.all()"
#["relationship_app/library_detail.html"