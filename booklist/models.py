from django.db import models
from django.contrib.auth.models import User

# variables
RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)

# Create your models here.
class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    author = models.CharField(max_length=50, null=True)
    picture = models.ImageField(null=True, upload_to='pictures/%Y/%m/')
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    
    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    
    def __str__(self):
        return '%s - %s' % (self.book.title, self.name)
    
class BookReview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    book = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True
    )
    rating = models.IntegerField(
        choices=RATING, default=None
    )
    
    def __str__(self):
        return self.book.title #type: ignore
    
    def get_rating(self):
        return self.rating