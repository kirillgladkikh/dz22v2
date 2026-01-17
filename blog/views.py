from django.shortcuts import render

from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import BlogPost
from .forms import BlogPostForm
from django.shortcuts import get_object_or_404


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/list.html"
    context_object_name = "posts"
    # paginate_by = 5

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by("-created_at")
        # return BlogPost.objects.using("blog").filter(is_published=True).order_by("-created_at")
        # return BlogPost.objects.all()  # вместо .filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        # Получаем объект стандартным способом (один запрос к БД)
        obj = super().get_object(queryset)

        # Увеличиваем просмотры и сохраняем
        obj.views_count += 1
        obj.save(update_fields=["views_count"])  # Только поле просмотров

        return obj

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     # Явно читаем из БД blog
    #     obj = BlogPost.objects.using("blog").get(pk=obj.pk)
    #
    #     # Увеличиваем просмотры
    #     obj.views_count += 1
    #     obj.save(using="blog", update_fields=["views_count"])
    #     return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/create.html"
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/update.html"
    success_url = reverse_lazy("blog:list")

    def get_object(self, queryset=None):
        # Достаточно одного вызова super().get_object()
        return super().get_object(queryset)

    def form_valid(self, form):
        print("POST data:", self.request.POST)
        print("Form cleaned_data:", form.cleaned_data)
        print("is_published in cleaned_data:", form.cleaned_data.get("is_published"))
        return super().form_valid(form)

    def get_success_url(self):
        # Возвращаем URL страницы детализации с текущим pk
        return reverse("blog:detail", kwargs={"pk": self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/delete.html"
    success_url = reverse_lazy("blog:list")

    def get_object(self, queryset=None):
        # Получаем объект стандартным способом (без лишних запросов)
        return super().get_object(queryset)

    def delete(self, request, *args, **kwargs):
        # Удаляем объект и выводим сообщение
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, "Запись удалена!")
        return super().delete(request, *args, **kwargs)
