from django.db import models

# Create your models here.
class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    author = models.CharField(max_length=50, null=True)
    picture = models.ImageField(null=True, blank=True, upload_to='pictures/%Y/%m/')
    
    def __str__(self):
        return f"{self.title}"