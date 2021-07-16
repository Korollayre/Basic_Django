from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm


def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


def admin_users(request):
    context = {'title': 'Админ-панель - Пользователи',
               'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Админ-панель - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update(request, pk):
    context = {'title': 'Админ-панель - Изменение пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_remove(request, pk):
    pass
