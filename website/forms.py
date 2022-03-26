from .models import Comment
from django import forms

# Credits - code is adapted from the CI LMS Django
# blog lessons and is fully accredited & acknowledged


class CommentForm(forms.ModelForm):
    """
    Class to enable data entry and collection via
    comment form with body field included
    """
    class Meta:
        model = Comment
        fields = ('body',)
