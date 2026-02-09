from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from catalog.models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category


class ProductsListView(TemplateView):
    template_name = "products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.select_related("owner").all()
        # context["products"] = Product.objects.all()
        context["is_product_card"] = False
        return context


class ProductCardView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_card.html"
    context_object_name = "product"

    def get_queryset(self):
        # Показываем только опубликованные продукты
        return Product.objects.filter(is_published=True)

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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()  # добавляем категории в контекст
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user  # автоматически устанавливаем владельца
        # form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_update.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()  # добавляем категории в контекст
        return context

    def form_valid(self, form):
        # Проверка права на отмену публикации
        if form.cleaned_data.get("is_published") is False:
            if not self.request.user.has_perm("catalog.can_unpublish_product"):
                form.add_error(None, "У вас нет прав на отмену публикации продукта.")
                return self.form_invalid(form)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != request.user and not request.user.has_perm("catalog.can_unpublish_product"):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("catalog:products_list")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != request.user:
            return self.handle_no_permission()
        return super().get(request, *args, **kwargs)


# class ProductDeleteView(LoginRequiredMixin, DeleteView):
#     model = Product
#     template_name = "product_delete.html"
#     success_url = reverse_lazy("catalog:products_list")
#
#     def dispatch(self, request, *args, **kwargs):
#         # Проверяем право на удаление
#         if (self.object.owner != request.user and
#             not request.user.has_perm("catalog.delete_product")):
#         # if (self.object.owner != request.user and not request.user.has_perm("catalog.delete_product")):
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)
