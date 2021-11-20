from django.db import models
from django.contrib.auth.models import User
from products.models import *
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=False)

    def __str__(self):
        return str(self.user.username)+ "" + str(self.total_price)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + "" + str(self.product.product_name)


@receiver(post_save,sender=CartItem)
def correct_price(sender,**kwargs):
    print("I got called")