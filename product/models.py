from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO

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
    image = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    """class Meta:
        ordering = ('-created_at',)
        #  puts the most recently added items at the top of frontpage... pretty neat!"""

    def __str__(self):
        return self.title
        #  display item title rather than Object (3)

    def get_display_price(self):
        return self.price / 100
        #  prices made by admin are originally in cents

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class ProductReview(models.Model):
    created_by = models.ForeignKey(User, null=True, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    review_image = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)



