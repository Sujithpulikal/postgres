from django import forms
from .models import Movieinfo

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movieinfo
        fields = '__all__'  # Include all fields in the model

        # Customize labels and widgets
        labels = {
            'title': 'Movie Title',
            'year': 'Release Year',
            'Review': 'Movie Summary',
            'img': 'Movie Poster',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie title',
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter release year',
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter movie summary',
            }),
            'img': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
