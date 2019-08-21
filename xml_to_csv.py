import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('../cookbook_import_pages_current.xml')
root = tree.getroot()

prefix = '{http://www.mediawiki.org/xml/export-0.10/}'
web_pages = [web_page for web_page in root.findall(prefix+'page') if web_page.find(prefix + 'ns').text=='0']

names = []
all_recipe_ingredients = []
for web_page in web_pages:
    names.append(web_page.find(prefix+'title').text)
    recipe = web_page.find(prefix+'revision').find(prefix+'text').text
    
def get_ingredients_from(recipe):
    ingredients = []
    for line in iter(recipe.splitlines(keepends=True)):
        if '= '+'Ingredient' or '=='+'Ingredient' in line:
            ingredients.append('Ingredient List')
            record_ingredients = True
        if record_ingredients==True and len(ingredients)==1:

    return ingredients

def get_instructions_from(recipe):
    for line in iter(recipe.splitlines(keepends=True)):
        if '= '+something or '=='+something in line:

def get_category_from(recipe):
    for line in iter(recipe.splitlines(keepends=True)):
        if '= '+something or '=='+something in line: 


d = {'Names': names, 'Recipes': recipes}
df = pd.DataFrame(data=d)
df.to_csv(path_or_buf=r'recipes.csv')
