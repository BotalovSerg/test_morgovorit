from django.db import models



class Recipes(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    count_using = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
class ProductToRecipe(models.Model):
    prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    rec = models.ForeignKey(Recipes, related_name='products', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)