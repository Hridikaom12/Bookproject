from django import forms
from .models import Book,Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']  


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            

        }