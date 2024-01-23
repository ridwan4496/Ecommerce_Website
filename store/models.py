from django.db import models
import datetime

# Catagories of Products
class Category(models.Model):
    category_name    = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'categories'

# Customer Details
class Customer(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    phone       = models.CharField(max_length=20)
    email       = models.EmailField(max_length=80)
    password    = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Products Details
class Product(models.Model):
    product_name    = models.CharField(max_length=250)
    price           = models.IntegerField(default=0)
    category_name   = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description     = models.TextField(max_length=1000, default='', blank=True, null=True)
    image           = models.ImageField(upload_to='uploads/product/')
    # Add Sale Stuffs
    is_sale         = models.BooleanField(default=False)
    sale_price      = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


# Customer Orders
class Order(models.Model):
    product_name    = models.ForeignKey(Product, on_delete=models.CASCADE,)
    customer        = models.ForeignKey(Customer, on_delete=models.CASCADE,)
    quantity        = models.IntegerField(default=1)
    address         = models.CharField(max_length=150, default='', blank=True)
    phone           = models.CharField(max_length=20, default='', blank=True)
    date            = models.DateField(default=datetime.datetime.today)
    status          = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
