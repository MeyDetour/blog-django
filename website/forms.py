from django import forms

from website.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "firstParagraphe", "secondParagraphe", "thirdParagraphe"]
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label="Username")
    password = forms.CharField(min_length=3,label="Pssword")