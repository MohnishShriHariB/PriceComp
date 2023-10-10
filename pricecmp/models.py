from django.db import models

# Create your models here.
class product(models.Model):
    type=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/pricecmp/images/')
    amazon_url=models.URLField(blank=True)
    flipkart_url=models.URLField(blank=True)
    amazon_price=models.CharField(blank=True,null=True,editable = False,max_length=100)
    flipkart_price=models.CharField(blank=True,null=True,editable = False,max_length=100)

    def __str__(self):
        return self.title
