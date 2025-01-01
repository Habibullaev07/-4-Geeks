from django.db import models

# Create your models here.


class PhotoMain(models.Model):
    image = models.ImageField(
        upload_to='photo_main/',
        verbose_name='фото'
    )
    def __str__(self):
        return f"{self.image}" 
    
    class Meta:
        verbose_name = "Фото (главного страницы)"
        verbose_name_plural = "Фото (главного страницы)"
        
