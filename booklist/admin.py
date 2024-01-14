from django.contrib import admin
from booklist import models

# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'year', 'created_at')
    ordering = '-id',
    list_filter = 'created_at',
    search_fields = ('id', 'title', 'genre', 'year',)
    list_per_page = 25
    list_max_show_all = 100

admin.site.register(models.Comment)
admin.site.register(models.BookReview)