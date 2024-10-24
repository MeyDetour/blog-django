from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    firstParagraphe = models.TextField()
    secondParagraphe = models.TextField()
    thirdParagraphe = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title

