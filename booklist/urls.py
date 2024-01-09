from django.urls import path
from booklist import views

app_name = 'booklist'

urlpatterns = [
    path('', views.index, name='index')
]
