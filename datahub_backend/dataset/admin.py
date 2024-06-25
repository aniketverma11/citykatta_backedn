from django.contrib import admin
from .models import *


class TagAdmin(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(Tag, TagAdmin)


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'upload_date')


admin.site.register(Dataset, DatasetAdmin)
