from django.shortcuts import render
from django.http import HttpResponse
from .models import ListRecipes, ListProducts



def all(request):
    res = ListRecipes.objects.all()
    context = {'res': res}
    print(res[0].recipes_one.get(id=1))
    return render(request, 'recipes/index.html', context=context)