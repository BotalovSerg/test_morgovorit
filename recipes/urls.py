from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.add_product_to_recipe, name="add_product"),
    path("cook/", views.cook_recipe, name="cook_recipe"),
    path("show/", views.show_recipes_without_product, name="show_recipe"),
]