from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(next_page='todolist:home'), name='login'),
    path("logout/", auth_views.logout_then_login, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register')
]
