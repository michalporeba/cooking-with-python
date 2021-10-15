import io
from .RecipeStore import RecipeStore 

class Rd1(RecipeStore):
    def read_all(self, file: io.TextIOWrapper) -> list:
        recipes = []
        recipe = {}
        for line in file.readlines():
            line = line.rstrip()
            if not line: 
                continue 
            key = line[:1]
            value = line[3:]
            if key == 'n':
                recipe = next((r for r in recipes if r['name'] == value), None)
                if not recipe and value:
                    recipe = { 'name': value, 'description': [], 'ingredients': [] }
                    recipes.append(recipe)
            elif key == 'd':
                recipe['description'].append(value)
            elif key == 'i':
                recipe['ingredients'].append(value)
        return recipes

    def save_all(self, file: io.TextIOWrapper, recipes: list):
        newline = '\n'
        for recipe in recipes: 
            file.write(f"n: {recipe['name']}"+newline)
            for desc in recipe['description']: 
                file.write(f"d: {desc}"+newline)
            for ingredient in recipe['ingredients']: 
                file.write(f"i: {ingredient}"+newline)