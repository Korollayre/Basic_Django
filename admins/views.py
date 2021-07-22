from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from products.models import ProductCategory
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductCategoryAdminForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Пользователи'
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Создание пользователя'
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Изменение пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Категории'
        return context


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryAdminForm
    template_name = 'admins/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_product_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Создание категории'
        return context


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryAdminForm
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_product_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Изменение категории'
        return context


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_product_category')
