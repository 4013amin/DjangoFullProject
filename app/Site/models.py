from django.db import models


# Create your models here.
class DataProductBanner(models.Model):
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=100)
    des = models.TextField()
    des2 = models.TextField()


class BlogData(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images/blog")

    def __str__(self):
        return self.name
