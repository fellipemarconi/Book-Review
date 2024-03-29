from django.urls import path
from booklist import views

app_name = 'booklist'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    # book (CRUD)
    path('book/<int:book_id>/', views.book_detail, name='book'),
    path('book/create/', views.book_create, name='create'),
    path('book/update/<int:book_id>/', views.book_update, name='update'),
    path('book/delete/<int:book_id>/', views.book_delete, name='delete'),
    
    #user
    path('user/login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    path('user/register/', views.register_user, name='register'),
    path('user/profile/', views.profile, name='profile'),
    path('user/delete/<int:pk>', views.user_delete, name='user_delete'),
    
    #comment
    path('book/delete_comment/<int:comment_pk>/', views.delete_comment, name='comment')
]
