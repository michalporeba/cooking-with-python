import io 
from .RecipeStore import RecipeStore

class Rd2(RecipeStore):
    def read_all(self, file: io.TextIOWrapper) -> list:
        recipes = []
        while True: 
            line = f.readline()
            if not line:
                break
            (description_lines, ingredients, name) = line.split(' ', 2)
            recipe = { 'name': name.strip(), 'description': [], 'ingredients': [] }
            for i in range(int(description_lines)):
                recipe['description'].append(file.readline().strip())
            for i in range(int(ingredients)):
                recipe['ingredients'].append(file.readline().strip())
            recipes.append(recipe)
        return recipes

    def save_all(self, file: io.TextIOWrapper, recipes: list):
        pass