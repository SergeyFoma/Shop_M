from django.contrib import admin
from goods.models import Categorys, Products

@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':("name",)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':("title",)}
