import requests
from pprint import pprint
from wpfunc import image_url, list_html_list, dict_list, wph2, headers
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
#pprint(ingredients)

# now work on instrucrtion

instruction_list = instruction.split('\r\n')
#print(instruction_list)
title = f'{meal_name} Recipie'
image = image_url(image, title)
heading_first = wph2('Ingredients')
ingredients_html = dict_list(ingredients)
heading_second = wph2('Description')
description = list_html_list(instruction_list)
content = f'{image}{heading_first}{ingredients_html}{heading_second}{description}'

data = {
    'title' : title,
    'content' : content
}
headers = headers('omor', 'USQu GRjv S1mR 6Kvs e1gb ye1b')
endpoint = 'https://mysite.local/wp-json/wp/v2/posts'
r = requests.post(endpoint, data=data, headers=headers, verify=False)
print(r)



