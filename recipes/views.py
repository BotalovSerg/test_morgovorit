from django.shortcuts import render
from recipes.models import Recipe, Product, Ingredient
from django.db.models import F
from django.db.models import Q



def home_page(request):
    """
    Отображает таблицу всех реуептов в базе данных
    """
    res = Recipe.objects.all()
    context = {'res': res}
    return render(request, 'recipes/home_page.html', context=context)


def add_product_to_recipe(request):
    """
    add_product_to_recipe с параметрами recipe_id, product_id, weight.
    Функция добавляет к указанному рецепту указанный продукт с указанным весом. 
    Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом 
    рецепте на указанный.
    пример запроса: recipes/add/?recipe_id=1&product_id=1&weight=888
    """
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')
    if recipe_id is None:
        return render(request, 'recipes/ok.html', context={
            'status' : 'Пустой запрос'
        })
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


def cook_recipe(request):
    """
    cook_recipe c параметром recipe_id.
    Функция увеличивает на единицу количество приготовленных блюд для каждого продукта,
    входящего в указанный рецепт.
    пример запроса: recipes/cook/?recipe_id=2
    """
    recipe_id = request.GET.get('recipe_id')
    question = Recipe.objects.get(pk=recipe_id)
    for item in question.ingredients.all():
        item.count_using = F('count_using') + 1
        item.save()
    context = {
        'status' : 'ok'
    }
    return render(request, 'recipes/ok.html', context=context)


def show_recipes_without_product(request):
    """
    show_recipes_without_product с параметром product_id.
    Функция возвращает HTML страницу, на которой размещена таблица. 
    В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, 
    или присутствует в количестве меньше 10 грамм. 
    Страница должна генерироваться с использованием Django templates.
    Качество HTML верстки не оценивается.
    пример запроса: recipes/show/?product_id=4
    """
    product_id = request.GET.get('product_id')
    recipes = Product.objects.get(pk=product_id).recipe_to.filter(weight__gte=10)
    list_recipes = [i.recipe.id for i in recipes]
    print(list_recipes)
    total = Recipe.objects.filter(~Q(pk__in=list_recipes))
    print(total)

    context = {
        'total' : total
    }

    return render(request, 'recipes/swow_recipes.html', context=context)