from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    def __str__(self):
        return self.variant_name

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)

    def __str__(self):
        return self.size_name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/products')
    price = models.PositiveIntegerField(default=0)
    desciption = models.TextField()
    stock = models.IntegerField(default=0)
    quantity_type = models.ForeignKey(QuantityVariant,on_delete=models.PROTECT,blank=True,null=True)
    color_type = models.ForeignKey(ColorVariant,on_delete=models.PROTECT,blank=True,null=True)
    size_type = models.ForeignKey(SizeVariant,on_delete=models.PROTECT,blank=True,null=True)

    class Meta:
        pass

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/products')
