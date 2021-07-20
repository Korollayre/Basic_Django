from django.urls import path

from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_users_remove, \
    admin_product_category, admin_product_category_create, admin_product_category_remove, admin_product_category_update

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:pk>/', admin_users_remove, name='admin_users_remove'),
    path('categories/', admin_product_category, name='admin_product_category'),
    path('categories/create/', admin_product_category_create, name='admin_product_category_create'),
    path('categories/update/<int:pk>/', admin_product_category_update, name='admin_product_category_update'),
    path('categories/remove/<int:pk>/', admin_product_category_remove, name='admin_product_category_remove'),
]
