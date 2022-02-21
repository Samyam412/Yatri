from django.db import models

# Create your models here.
class carouselImage(models.Model):
    image = models.ImageField(upload_to='carouselImage',null=False,blank=False)

    def __str__(self):
        return f'{self.image}'

class carouselImage2(models.Model):
    image2 = models.ImageField(upload_to='carouselImage2',null=False,blank=False)

    def __str__(self):
        return f'{self.image2}'