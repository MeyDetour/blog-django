from django import forms
from django.contrib.auth.models import User

from website.models import Article, Comment, Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "firstParagraphe", "secondParagraphe", "thirdParagraphe", "image","tag"]
    image = forms.ImageField(required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Ici, 'content' est un champ du modèle Comment.


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username",widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(min_length=3, label="Pssword", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Username", min_length=2)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']