import secrets

from django.shortcuts import get_object_or_404, redirect, reverse
from django.core.mail import send_mail

from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import UserRegisterForm
from user.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/user/email-confirm/{token}/"

        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("user:login"))


# from django.http import HttpResponse
#
#
# def user(request):
#     return HttpResponse("Привет из приложения user!")
