from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .forms import BookForm
from .models import Book

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # your logic
     book = get_object_or_404(Book, pk=pk)

     if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # replace with your actual URL name
     else:
        form = BookForm(instance=book)

     return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})


# Create your views here.