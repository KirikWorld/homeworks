from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipe(request, food):
    recipe_dict = DATA[food].copy()
    servings = request.GET.get('servings', 1)
    # print(servings)
    for key, val in recipe_dict.items():
        recipe_dict[key] = val * int(servings)
    context = {
        'recipe': recipe_dict
    }
    # result = str(recipe_dict)
    # result = result.replace(", '", "<br>").strip('{}').replace("'", "")
    # return HttpResponse(f'{result}')
    return render(request, 'index.html', context=context)
