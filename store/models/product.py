from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='/uploads')
    category = models.CharField()

    def __str__(self):
        return self.name

    def display_product(self):
        return self.name, "\n", self.description, "\n", self.price

