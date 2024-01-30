from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=255)
    count_using = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Product, through='Ingredient')

    def __str__(self) -> str:
        return self.name
    
    
class Ingredient(models.Model):
    product = models.ForeignKey(Product, related_name='recipe_to', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='products', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)