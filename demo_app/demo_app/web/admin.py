from django.contrib import admin

from demo_app.web.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
