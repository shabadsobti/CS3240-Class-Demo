from django.db import models

# Create your models here.

class Meme(models.Model):
    text = models.CharField(max_length=50)
    image_url = models.URLField(null=True)
