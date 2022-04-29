from django import forms

from .models import Tag, Comment, News


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'text']
