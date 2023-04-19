from django.db import models

# Create your models here.
class Post(models.Model):
    Title   = models.CharField(max_length=100)
    Content = models.TextField(max_length=5000)
    Image   = models.ImageField(upload_to="posts\\")

    def __str__(self):
        return self.Title