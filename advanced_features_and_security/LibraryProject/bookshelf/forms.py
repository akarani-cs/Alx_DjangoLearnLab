from django import forms



class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100, required=True, help_text="Enter an example value.")
    
    def clean_example_field(self):
        data = self.cleaned_data['example_field']
        if not data.isalnum():
            raise forms.ValidationError("This field must contain only alphanumeric characters.")
        return data