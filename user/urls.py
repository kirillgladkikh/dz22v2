from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user.apps import UserConfig
from user.views import UserCreateView
from user.forms import LoginForm
from . import views


app_name = UserConfig.name

urlpatterns = [
    # path('', views.user, name='user'),  # пример маршрута
    # path('login/', LoginView.as_view(template_name="login.html")),
    # path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('login/', LoginView.as_view(authentication_form=LoginForm, template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
]
