from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class PostForm(forms.ModelForm):
    # Comma-separated input (e.g., "django, auth, tips")
    tags_input = forms.CharField(
        required=False,
        help_text="Comma-separated (e.g. django, auth, tips)"
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags_input"]

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # apply tags
        tags_str = self.cleaned_data.get("tags_input", "")
        names = [t.strip() for t in tags_str.split(",") if t.strip()]
        if names:
            instance.tags.set(names)  # taggit accepts list of names
        else:
            instance.tags.clear()
        return instance