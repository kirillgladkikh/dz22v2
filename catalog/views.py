from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "base.html", context)


def home(request):
    """Список товаров"""
    products = Product.objects.all()
    context = {
        'products': products,
        'is_product_card': False,  # Флаг: это НЕ детальная страница = НЕ product_card.html
    }
    # context = {"products": products}
    return render(request, "home.html", context)


def product_card(request, pk):
    """Детальная страница товара"""
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'is_product_card': True,   # Флаг: это детальная страница = product_card.html !
    }
    return render(request, 'product_card.html', context)




# def product_list(request):
#     """Главная страница — список товаров"""
#     products = Product.objects.all()
#     context = {
#         'products': products,
#         'is_detail_page': False,  # Флаг: это НЕ детальная страница
#     }
#     return render(request, 'myapp/product_list.html', context)
#
# def product_detail(request, pk):
#     """Детальная страница товара"""
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product,
#         'is_detail_page': True,   # Флаг: это детальная страница
#     }
#     return render(request, 'myapp/product_detail.html', context)





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
