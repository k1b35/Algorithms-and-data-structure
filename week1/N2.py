import sys


def can_cook_recipes(products, recipes):
    available_products = set(products)
    cookable_recipes = []

    for recipe in recipes:
        recipe_name = recipe[0]
        ingredients = recipe[2:]

        if all(ingredient in available_products for ingredient in ingredients):
            cookable_recipes.append(recipe_name)

    return cookable_recipes



lines = sys.stdin.readlines()
input_data = [line.strip() for line in lines]


num_products = int(input_data[0])
products = input_data[1:num_products + 1]

num_recipes = int(input_data[num_products + 1])
recipes = []
start_index = num_products + 2
i = 0
while i < num_recipes:
    recipe_name = input_data[start_index + (i * 2)]
    num_ingredients = 0
    try:
        num_ingredients = int(input_data[start_index + (i * 2) + 1])
    except ValueError:
        i += 1
        continue
    ingredients = input_data[start_index + (i * 2) + 2: start_index + (i * 2) + 2 + num_ingredients]
    recipes.append((recipe_name, num_ingredients, *ingredients))
    i += 1


cookable_recipes = can_cook_recipes(products, recipes)


for recipe in cookable_recipes:
    print(recipe)
