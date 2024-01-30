from django.contrib import admin
from .models import Product, Recipe, Ingredient


# class ProductRecipeInline(admin.TabularInline):
#     model = ProductToRecipe
#     raw_id_fields = ['rec']



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']