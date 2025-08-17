from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .forms import RegisterForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.db.models import Q


# ✅ Register view
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect("login")  # redirect to login page
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


# ✅ Login & Logout are handled using Django's built-in class-based views
# In urls.py you'll map:
# path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login")
# path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout")


# ✅ Profile view (requires login)
@login_required
def profile(request):
    return render(request, "blog/profile.html")


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        return self.get_object().author == self.request.user
    
    def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag]).select_related("author").prefetch_related("tags")
    return render(request, "blog/post_list.html", {"posts": posts, "active_tag": tag})

  def search(request):
    query = request.GET.get("q", "").strip()
    posts = Post.objects.none()
    if query:
        posts = (
            Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)  # taggit name lookup
            )
            .distinct()
            .select_related("author")
            .prefetch_related("tags")
        )
    return render(request, "blog/search_results.html", {"posts": posts, "query": query})