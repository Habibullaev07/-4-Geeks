from django.contrib import admin
from django.utils.html import format_html
from apps.main.models import PhotoMain

# Register your models here.

@admin.register(PhotoMain)
class PhotoMainAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))
    
    list_display = ("image_tag",)