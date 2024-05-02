from django.db import models
from django.urls import reverse


# Create your models here.
class Kinds(models.Model):
    kinds = models.CharField(max_length=60)

    def __str__(self):
        return self.kinds


class Products(models.Model):
    photo = models.ImageField(upload_to='prouct_photo')
    kind = models.ForeignKey(Kinds, on_delete=models.CASCADE)
    body = models.TextField()
    price = models.IntegerField()
    counts = models.IntegerField()

    def __str__(self):
        return str(self.kind)

    def get_absolute_url(self):
        return reverse('news_detail_page', args=[self.id])



class AboutCandyShop(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    shop_photo = models.ImageField(upload_to='about_candy_shop')
    location = models.CharField(max_length=255)


    def __str__(self):
        return self.name








