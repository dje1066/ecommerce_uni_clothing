from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)  # URL representation of title field above (i.e. 8000/wool-lined-jacket/)

    class Meta:
        verbose_name_plural = 'Categories'
        # fixed misspelling in view - Categorys

    def __str__(self):
        return self.title


class Product(models.Model):
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # related name = easier to get all items for the category
    # on_delete CASCADE = if category is deleted, then the items within it are all deleted too

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)

    """class Meta:
        ordering = ('-created_at',)
        #  puts the most recently added items at the top of frontpage... pretty neat!"""

    def __str__(self):
        return self.title
        #  display item title rather than Object (3)

    def get_display_price(self):
        return self.price / 100
        #  prices made by admin are originally in cents
