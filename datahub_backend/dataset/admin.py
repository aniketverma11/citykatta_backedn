from django.contrib import admin
from .models import *


class TagAdmin(admin.ModelAdmin):
    fields = ('name',)

admin.site.register(Tag, TagAdmin)

class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'upload_date')

admin.site.register(Dataset, DatasetAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('dataset', 'reviewer', 'rating', 'created_at')


admin.site.register(Review, ReviewAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'description', 'contact_email', 'website')

admin.site.register(Provider, ProviderAdmin)
