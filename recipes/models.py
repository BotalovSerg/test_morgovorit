from django.db import models



class ListRecipes(models.Model):
    name = models.CharField(max_length=200)   

    def __str__(self) -> str:
        return self.name
    
class ListProducts(models.Model):
    name = models.CharField(max_length=200)
    count_using = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
class ProductToRecipe(models.Model):
    product = models.ForeignKey(ListProducts, related_name='product_to_recipe', on_delete=models.CASCADE)
    recipe = models.ForeignKey(ListRecipes, related_name='recipes_one', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return str(self.id)