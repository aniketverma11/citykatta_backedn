from django.contrib import admin
from .models import *


class TagAdmin(admin.ModelAdmin):
    fields = ("name",)


class DatasetAdmin(admin.ModelAdmin):
    list_display = ("name", "provider", "upload_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


class UseCaseAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(UseCase, UseCaseAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
