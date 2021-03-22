from django import forms

from mysite.Article.models import Article

class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text',)