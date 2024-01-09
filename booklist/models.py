from django.db import models

# Create your models here.
class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.title}"