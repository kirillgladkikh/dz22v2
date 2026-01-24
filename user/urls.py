from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user.apps import UserConfig
from . import views


app_name = UserConfig.name

urlpatterns = [
    path('', views.user, name='user'),  # пример маршрута
    # path('login/', LoginView.as_view(template_name="login.html")),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]








# пример
# urlpatterns = [
#     path("", views.BlogPostListView.as_view(), name="list"),
#     path("create/", views.BlogPostCreateView.as_view(), name="create"),
#     path("<int:pk>/", views.BlogPostDetailView.as_view(), name="detail"),
#     path("<int:pk>/update/", views.BlogPostUpdateView.as_view(), name="update"),
#     path("<int:pk>/delete/", views.BlogPostDeleteView.as_view(), name="delete"),
# ]
