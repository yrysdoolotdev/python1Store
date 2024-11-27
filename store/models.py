from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    have = models.BooleanField()
    img = models.ImageField(upload_to='img/', null=True, blank=True)
    video = models.FileField(upload_to='product_videos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name}, {self.price}'


