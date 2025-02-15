from django.urls import path
from users import views

app_name="users"

urlpatterns=[
    path('login/', views.login, name='login'),
    path('registrations/', views.registrations, name='registrations'),
    path('profile/', views.profile, name='profile'),
    path('users_cart/', views.users_cart, name='users_cart'),
    path('logout/', views.logout, name='logout'),
]