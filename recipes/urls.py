from django.urls import path

from . import views

urlpatterns = [
    path("", views.add_product_to_recipe, name="add_product"),
]