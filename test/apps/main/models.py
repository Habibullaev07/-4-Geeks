from django.db import models

# Create your models here.

class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Имя заголовка"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главной"
        verbose_name_plural = "Главное"