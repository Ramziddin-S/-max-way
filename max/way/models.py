from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    combo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=110, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    foods = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    products = models.JSONField(blank=False, null=False)
    status = models.IntegerField(blank=False, null=False, default=1)
    total_price = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    first_name = models.CharField(max_length=120, blank=False, null=False)
    last_name = models.CharField(max_length=130, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100, blank=False, null=False)
    price_type = models.PositiveIntegerField(blank=False, null=False, default=0)
    order = models.ForeignKey(Order, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name
