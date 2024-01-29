from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.all, name="all_list"),
    path("cook/<int:id_recipet>/", views.get_recipet, name="cook_reci"),
]