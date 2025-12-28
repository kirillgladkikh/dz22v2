from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product


# Create your views here.
def products_list(request):
    """Список товаров"""
    products = Product.objects.all()
    context = {
        "products": products,
        "is_product_card": False,  # Флаг: это НЕ детальная страница = НЕ product_card.html
    }
    return render(request, "products_list.html", context)


def product_card(request, pk):
    """Детальная страница товара"""
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
        "is_product_card": True,  # Флаг: это детальная страница = product_card.html !
    }
    return render(request, "product_card.html", context)


def contacts(request):
    """Отправка контактов"""
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
