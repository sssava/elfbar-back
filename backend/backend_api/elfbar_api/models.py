from django.db import models

# Create your models here.


class Taste(models.Model):
    name = models.CharField(max_length=150)
    count_in_stock = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Elfbar(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(default='default.png', null=True, blank=True)
    taste = models.ForeignKey(Taste, on_delete=models.SET_NULL, null=True)
    charge = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    nicotine = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.postal_code}"


class OrderItem(models.Model):
    elfbar = models.ForeignKey(Elfbar, on_delete=models.CASCADE, related_name="elfbar")
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")

    def __str__(self):
        return f"Postal Code: {self.order.postal_code}, Elfbar: {self.elfbar.name}, Quantity: {self.quantity}"
