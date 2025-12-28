from django.shortcuts import render

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import BlogPost
from .forms import BlogPostForm


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return BlogPost.objects.using('blog').filter(is_published=True).order_by('-created_at')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Явно читаем из БД blog
        obj = BlogPost.objects.using('blog').get(pk=obj.pk)

        # Увеличиваем просмотры
        obj.views_count += 1
        obj.save(using='blog', update_fields=['views_count'])
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.save(using='blog')  # Явно сохраняем в БД blog
        messages.success(self.request, 'Запись успешно создана!')
        return response


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return BlogPost.objects.using('blog').get(pk=obj.pk)  # Читаем из БД blog

    def form_valid(self, form):
        form.save(using='blog')  # Явно сохраняем в БД blog
        messages.success(self.request, 'Запись обновлена!')
        return super().form_valid(form)


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return BlogPost.objects.using('blog').get(pk=obj.pk)  # Читаем из БД blog

    def delete(self, request, *args, **kwargs):
        self.get_object().delete(using='blog')  # Явно удаляем из БД blog
        messages.success(request, 'Запись удалена!')
        return super().delete(request, *args, **kwargs)




# class BlogPostListView(ListView):
#     model = BlogPost
#     template_name = 'blog/list.html'
#     context_object_name = 'posts'
#
#     paginate_by = 5
#
#     def get_queryset(self):
#         return BlogPost.objects.filter(is_published=True).order_by('-created_at')
#
#
# class BlogPostDetailView(DetailView):
#     model = BlogPost
#     template_name = 'blog/detail.html'
#     context_object_name = 'post'
#
#
#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset)
#         obj.views_count += 1
#         obj.save(update_fields=['views_count'])
#         return obj
#
#
# class BlogPostCreateView(SuccessMessageMixin, CreateView):
#     model = BlogPost
#     form_class = BlogPostForm
#     template_name = 'blog/create.html'
#     success_url = reverse_lazy('blog:list')
#     success_message = "Запись успешно создана!"
#
#
# class BlogPostUpdateView(SuccessMessageMixin, UpdateView):
#     model = BlogPost
#     form_class = BlogPostForm
#     template_name = 'blog/update.html'
#     success_url = reverse_lazy('blog:list')
#     success_message = "Запись успешно обновлена!"
#
#
# class BlogPostDeleteView(DeleteView):
#     model = BlogPost
#     template_name = 'blog/delete.html'
#     success_url = reverse_lazy('blog:list')
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = f'Удалить "{self.object.title}"?'
#         return context
