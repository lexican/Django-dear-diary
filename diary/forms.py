from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):
    text = forms.CharField(label='Post', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'What\'s on your mind?',
        'id': 'post',
        'rows': '4',
    }))

    class Meta:
        model = Post
        fields = ('text', )