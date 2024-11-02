from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    firstParagraphe = models.TextField(verbose_name="Premier Paragraphe")
    secondParagraphe = models.TextField(verbose_name="Deuxième Paragraphe")
    thirdParagraphe = models.TextField(verbose_name="Troisième Paragraphe")
    image = models.ImageField(upload_to='images/', verbose_name="Image de l'article",blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Auteur")


    def __str__(self):
                return self.title



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'