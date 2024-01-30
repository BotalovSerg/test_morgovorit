from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from recipes.models import Recipe, Product, Ingredient



def home_page(request):
    res = Recipe.objects.all()
    context = {'res': res}
    return render(request, 'recipes/home_page.html', context=context)


def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')
        question = Ingredient.objects.filter(recipe=recipe_id, product=product_id)
        if question:
            obj = question[0]
            obj.weight = weight
            obj.save()
        else:
            Ingredient.objects.create(
                product=Product.objects.get(pk=product_id),
                recipe=Recipe.objects.get(pk=recipe_id),
                weight=weight,
            )
    context = {
        'status' : 'ok'
    }
    return render(request, 'recipes/ok.html', context=context)


#   add_product_to_recipe с параметрами recipe_id, product_id, weight. 
# recipes/?recipe_id=2&product_id=6&weight=44
# Функция добавляет к указанному рецепту указанный продукт с указанным весом. 
# Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом 
# рецепте на указанный.