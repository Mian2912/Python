from django.contrib import admin

# Register your models here.
from .models import Pages
# Register your models here.
class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')

admin.site.register(Pages, PagesAdmin)