from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from recipes.models import ListRecipes, ListProducts



def all(request):
    res = ListRecipes.objects.all()
    context = {'res': res}
    return render(request, 'recipes/index.html', context=context)

def get_recipet(request, id_recipet):
    question = get_object_or_404(ListRecipes, id=id_recipet)
    cook = question.name
    # for i in question.recipes_one.all():
    #     print(i.product_id)
    listproducts = [ListProducts.objects.get(id=i.product_id) for i in question.recipes_one.all()]
    context = {
         'cook': cook,
         'listproducts': listproducts
    }
    return render(request, 'recipes/one.html', context=context)