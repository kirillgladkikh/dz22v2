from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from catalog.models import Product
from .forms import ProductForm

from .models import Category


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
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # добавляем категории в контекст
        return context

    def form_valid(self, form):
        # print("POST data:", self.request.POST)  # Что пришло из формы
        # print("Form cleaned_data:", form.cleaned_data)  # Что обработала форма
        # print("is_published in cleaned_data:", form.cleaned_data.get("is_published"))
        return super().form_valid(form)

    # def form_valid(self, form):
    #     # form.save()  # Django сам сохранит и объект, и изображение
    #     return super().form_valid(form)
    # def form_valid(self, form):
    #     product = form.save(commit=False)  # создаём объект продукта, но не сохраняем сразу
    #     product.category_id = self.request.POST.get('category')  # присваиваем ID категории из POST-запроса
    #     product.save()  # сохраняем продукт с привязанной категорией
    #     return super().form_valid(form)  # завершаем обработку (редирект на success_url)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # добавляем категории в контекст
        return context

    def form_valid(self, form):
        # print("POST data:", self.request.POST)
        # print("Form cleaned_data:", form.cleaned_data)
        # print("is_published in cleaned_data:", form.cleaned_data.get("is_published"))
        return super().form_valid(form)
    # def form_valid(self, form):
    #     # form.save()  # Django сам сохранит и объект, и изображение
    #     return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:products_list')


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
