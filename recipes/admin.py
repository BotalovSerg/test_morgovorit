from django.contrib import admin
from .models import Products, Recipes, ProductToRecipe


class ProductRecipeInline(admin.TabularInline):
    model = ProductToRecipe
    raw_id_fields = ['rec']



@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    inlines = [ProductRecipeInline]

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'count_using']