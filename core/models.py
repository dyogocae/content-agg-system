from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    webpage = models.TextField(max_length=99, default="") 
    url = models.TextField(max_length=255)
    image = models.URLField(null=True, blank=True)