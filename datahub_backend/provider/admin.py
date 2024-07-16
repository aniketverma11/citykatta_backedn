from django.contrib import admin

from datahub_backend.provider.models import Review, ProviderModel


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("dataset", "reviewer", "rating", "created_at")


admin.site.register(Review, ReviewAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ("owner", "designation", "company")


admin.site.register(ProviderModel, ProviderAdmin)
