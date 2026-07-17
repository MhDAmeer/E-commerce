from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    

    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'comment']
        widgets = {
            'reviewer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
            }),
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'form-select'},
            ),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review here...',
            }),
        }
