from django.contrib import admin
from .models import Category, Product, Network, Main, Our


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'date_update')
    fields = ('name', 'slug', 'text', 'img')
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'date', 'date_update')
    fields = ('name', 'price', 'text', 'img', 'category')


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'date_update')
    fields = ('name', 'network')


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'date_update')
    fields = ('name', 'text')


@admin.register(Our)
class OurAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'date_update')
    fields = ('name', 'text')