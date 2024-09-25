from django.db import models


# Create your models here.
class DataProductBanner(models.Model):
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=100)
    des = models.TextField()
    des2 = models.TextField()


class ProductTop(models.Model):
    image = models.ImageField(upload_to="images/top")
    descount = models.IntegerField()
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    listDes1 = models.CharField(max_length=100)
    listDes2 = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
