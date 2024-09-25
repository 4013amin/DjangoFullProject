from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.DataProductBanner)
class DataProductBannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'des')


@admin.register(models.BlogData)
class BlogDataAdmin(admin.ModelAdmin):
    list_display = ('name',)
