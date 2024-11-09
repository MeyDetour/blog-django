from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

import os
import re

def validate_image_type(image):
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'webp']
    extension = image.name.split('.')[-1].lower()

    if extension not in valid_extensions:
        raise ValidationError(f"Invalid file type: {extension}. Only jpg, jpeg, png, gif, and webp are allowed.")

def get_clean_filename(instance, filename):
    # Supprimer les caractères spéciaux et garder le nom du fichier court
    name, extension = os.path.splitext(filename)
    name = re.sub(r'[^a-zA-Z0-9_-]', '', name)  # Garder uniquement des caractères sûrs
    return f'images/{name}_{instance.id}{extension}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    firstParagraphe = models.TextField(verbose_name="Premier Paragraphe")
    secondParagraphe = models.TextField(verbose_name="Deuxième Paragraphe",blank=True)
    thirdParagraphe = models.TextField(verbose_name="Troisième Paragraphe",blank=True)
    image = models.ImageField(upload_to=get_clean_filename, verbose_name="Image de l'article",blank=True,validators=[validate_image_type])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Auteur")
    tag = models.CharField(max_length=100, verbose_name="Tag")

    def __str__(self):
                return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'