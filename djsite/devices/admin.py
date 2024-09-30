from django.contrib import admin
from .views import *

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cat", "photo", "is_published")
    list_display_links = ("name",)
    fields = ("name", "cat", "photo")
    list_editable = ("is_published",)

    def get_category(self, obj):
        return obj.cat.category

    get_category.short_description = 'Category'

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=200>")

    get_html_photo.short_description = "Photo"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
    fields = ("category",)


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "device", "description_paragraph")


admin.site.register(Device, DeviceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Description, DescriptionAdmin)
