from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home_v, register_v,  logout_v

urlpatterns = [
  path('', home_v, name="home"),
  path('register/', register_v, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
  path('logout/', logout_v, name='logout'),
]