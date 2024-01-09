from django.urls import path
from booklist import views

app_name = 'booklist'

urlpatterns = [
    path('', views.index, name='index'),
    
    #user
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
