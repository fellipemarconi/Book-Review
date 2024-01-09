from django.urls import path
from booklist import views

app_name = 'booklist'

urlpatterns = [
    path('', views.index, name='index'),
    
    #user
    path('user/login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    path('user/register/', views.register_user, name='register'),
]
