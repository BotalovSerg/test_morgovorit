from django.contrib import admin
from .models import ListProducts, ListRecipes, ProductToRecipe


class ProductRecipeInline(admin.TabularInline):
    model = ProductToRecipe
    raw_id_fields = ['recipe']



@admin.register(ListRecipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    inlines = [ProductRecipeInline]

@admin.register(ListProducts)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'count_using']