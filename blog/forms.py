from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Content',
                'class': 'new-class-name two',
                'id': 'my-id-for-text-area',
                'rows': 5,
                'cols': 120,
            }
        )
    )
    author = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Author Name'}))

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'author'
        ]