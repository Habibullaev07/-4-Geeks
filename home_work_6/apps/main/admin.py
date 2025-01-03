from django.contrib import admin
from django.utils.html import format_html
from apps.main.models import Main, Over, Awards, About, AwardsBottom, Direction, Graduated
# Register your models here.

admin.site.register(Main)
admin.site.register(Over)

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))
    
    # fields = ['image_tag']
    list_display = ("image_tag",)
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def video_tag(self, obj):
        return format_html('<video src="{}" width="auto" height="50px" />'.format(obj.video.url))
    
    list_display = ('title', 'description', 'video_tag')


@admin.register(AwardsBottom)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'awards')
    
@admin.register(Direction)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
@admin.register(Graduated)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('years_graduated', 'name', 'direction')