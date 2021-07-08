from django.db import models
from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price


def total_quantity(basket, amount=0):
    for el in basket:
        amount += el.quantity
    return amount


def total_sum(basket, amount=0):
    for el in basket:
        amount += el.quantity * el.product.price
    return amount