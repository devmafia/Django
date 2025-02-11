from django.urls import path
from .views import home, create_post, edit_post, delete_post
from .views import register, user_login, user_logout, edit_profile, contact, feedback

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:pk>/', edit_post, name='edit_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('register/', register, name='register'),
    path('accounts/login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('contact/', contact, name='contact'),
    path('feedback/', feedback, name='feedback'),
]
