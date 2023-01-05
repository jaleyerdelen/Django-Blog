from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home","slug",)
    list_editable = ("is_home", "is_active",)
    search_fields = ("title", "description",)
    readonly_fields = ("slug",)
    list_filters = ("category","is_active","is_home",)
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
