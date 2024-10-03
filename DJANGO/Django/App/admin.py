from django.contrib import admin
from .models import AppVariety, AppCertificate, AppReview, Store

# Register your models here.

class AppReviewInline(admin.TabularInline):
    model = AppReview
    extra = 1

class AppVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added', 'model')
    inlines = [AppReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('app_varities',)

class AppCertificateAdmin(admin.ModelAdmin):
    list_display = ('app', 'certificate_num')


admin.site.register(AppVariety, AppVarietyAdmin)
admin.site.register(AppCertificate, AppCertificateAdmin)
admin.site.register(Store, StoreAdmin)