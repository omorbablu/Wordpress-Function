#there take the single or 1st meals all information

import requests
from pprint import pprint
api_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'
r= requests.get(api_url)
meals = r.json().get('meals')
#pprint(meals)

single_meal = meals[0]
#pprint(single_meal)
meal_name = single_meal.get('strMeal')
meal_area = single_meal.get('strArea')
meal_category = single_meal.get('strCategory')
instruction = single_meal.get('strInstructions')
image = single_meal.get('strMealThumb')
youtube = single_meal.get('strYoutube')

i = 1
ingredients = {}
while i < 21:
    key_ingredients = f'strIngredient{i}'
    key_measurements = f'strMeasure{i}'

    if (single_meal.get(key_ingredients) != None) and (single_meal.get(key_ingredients) != ""):
        #print(single_meal.get(key_ingredients))
        ingredients[single_meal.get(key_ingredients)] = single_meal.get(key_measurements)
    i +=1
pprint(ingredients)