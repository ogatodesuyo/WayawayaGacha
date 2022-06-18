from django.contrib import admin
from .models import Category, SubCategory, Menu

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug': ('name',)}


admin.site.register(SubCategory, SubCategoryAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available']
    list_editable = ['price', 'available']
    prepopulated_field = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Menu, MenuAdmin)