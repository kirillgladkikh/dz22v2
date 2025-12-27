from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "base.html", context)


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)


# def index(request):
#     return render(request, "base.html")


# def home(request):
#     return render(request, "home.html")


def contacts(request):
    # return render(request, 'contacts.html')
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"Спасибо, {name}! \
            Ваш телефон: {phone}. \
            Сообщение получено: {message}."
        )

    return render(request, "contacts.html")
