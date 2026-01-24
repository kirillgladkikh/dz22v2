from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import UserRegisterForm
from user.models import User

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')


# from django.http import HttpResponse
#
#
# def user(request):
#     return HttpResponse("Привет из приложения user!")
