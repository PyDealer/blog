from django import forms
from django.utils import timezone

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'category', 'location', 'image']
        widgets = {
            'pub_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'value':
                       timezone.now().strftime('%Y-%m-%dT%H:%M')})
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['pub_date'].input_formats = ('%Y-%m-%dT%H:%M',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
