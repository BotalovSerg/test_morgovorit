from django.contrib import admin
from .models import Product, Recipe, Ingredient


class ProductRecipeInline(admin.TabularInline):
    model = Ingredient
    raw_id_fields = ['recipe']



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [
        ProductRecipeInline,
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'count_using']