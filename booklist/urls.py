from django.urls import path
from booklist import views

app_name = 'booklist'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    # book (CRUD)
    path('book/<int:book_id>', views.book_detail, name='book'),
    
    #user
    path('user/login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    path('user/register/', views.register_user, name='register'),
    path('user/profile/', views.profile, name='profile'),
]
