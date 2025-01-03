from email.mime import image
from pyexpat import model
from django.db import models

# Create your models here.


class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    banner = models.ImageField(
        upload_to='banner/',
        verbose_name='Фото баннера'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка Главной"
        verbose_name_plural = "Настройки Главной"
        
class Over(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    date = models.CharField(
        max_length=255,
        verbose_name='Год'
    )
    direction = models.CharField(
        max_length=255,
        verbose_name='Направление'
    )
    img = models.ImageField(
        upload_to='over/',
        verbose_name="Фото"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Анимация"
        verbose_name_plural = "Анимации"

class Awards(models.Model):
    image = models.ImageField(
        upload_to='awards/',
        verbose_name='фото'
    )
    def __str__(self):
        return f"{self.image}" 
    
    class Meta:
        verbose_name = "О нас (галерея)"
        verbose_name_plural = "О нас (галерея)"
        
        
class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    video = models.FileField(
        upload_to='video/',
        verbose_name="Видео"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        
        
class AwardsBottom(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание награды'
    )
    awards = models.TextField(
        verbose_name="Награды"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Награды"
        verbose_name_plural = "Награды"
        
class Direction(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название направление"
    )
    description = models.TextField(
        verbose_name="Описание вашего направление"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направление"
    
    
class Graduated(models.Model):
    years_graduated = models.TextField(
        verbose_name="Год окончание"
    )
    name = models.CharField(
        max_length=30,
        verbose_name="Имя ученика окончившийся"
    )
    direction = models.TextField(
        verbose_name="Направление студента"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Окончившийся"
        verbose_name_plural = "Окончившийся"