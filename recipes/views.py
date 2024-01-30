from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from recipes.models import Recipe, Product



def all(request):
    res = Recipe.objects.all()
    context = {'res': res}
    return render(request, 'recipes/index.html', context=context)

def get_recipet(request, id_recipet):
    question = get_object_or_404(Recipe, id=id_recipet)
    cook = question.name
    # for i in question.recipes_one.all():
    #     print(i.product_id)
    listproducts = [Product.objects.get(id=i.product_id) for i in question.recipes_one.all()]
    context = {
         'cook': cook,
         'listproducts': listproducts
    }
    return render(request, 'recipes/one.html', context=context)

def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')
        question = get_object_or_404(Recipe, id=recipe_id)
        listproducts = [Product.objects.get(id=i.product_id).name for i in question.recipes_one.all()]
        print(listproducts)


    return render(request, 'recipes/ok.html')