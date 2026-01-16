from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from catalog.models import Product
from .forms import ProductForm


class ProductsListView(TemplateView):
    template_name = "products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["is_product_card"] = False
        return context


class ProductCardView(DetailView):
    model = Product
    template_name = "product_card.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_product_card"] = True
        return context


class ContactsView(View):
    template_name = "contacts.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо, {name}! \
            Ваш телефон: {phone}. \
            Сообщение получено: {message}."
        )


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products_list')


# from django.views import View
# from django.views.generic import TemplateView, DetailView
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from catalog.models import Product
#
#
# class ProductsListView(TemplateView):
#     template_name = "products_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = Product.objects.all()
#         context["is_product_card"] = False
#         return context
#
#
# class ProductCardView(DetailView):
#     model = Product
#     template_name = "product_card.html"
#     context_object_name = "product"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["is_product_card"] = True
#         return context
#
#
# class ContactsView(View):
#     template_name = "contacts.html"
#
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         return HttpResponse(
#             f"Спасибо, {name}! \
#             Ваш телефон: {phone}. \
#             Сообщение получено: {message}."
#         )
