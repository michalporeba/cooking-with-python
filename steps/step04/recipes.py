recipes = []
has_changes = False
filename = 'recipes.rd2'

if filename.endswith('.rd1'):
    with open(filename) as f: 
        recipe = {}
        for line in f.readlines():
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

if filename.endswith('.rd2'):
    with open(filename) as f:
        while True: 
            line = f.readline()
            if not line:
                break
            (description_lines, ingredients, name) = line.split(' ', 2)
            recipe = { 'name': name.strip(), 'description': [], 'ingredients': [] }
            for i in range(int(description_lines)):
                recipe['description'].append(f.readline().strip())
            for i in range(int(ingredients)):
                recipe['ingredients'].append(f.readline().strip())
            recipes.append(recipe)
        
def display_recipes() -> dict:
    print("Available recipes:")
    for i, recipe in enumerate(recipes):
        print(f"\t{i+1} - {recipe['name']}")

def get_users_choice(number_of_recipes: int) -> (str, int): 
    while True:
        print("\n(choose recipe number to see it, type 'add' to add a new one, or press enter to exit)")
        choice = input("which recipe would you like to see?\n")
        if not choice:
            return ('exit', None)
        elif choice == 'add':
            return ('add', None)
        elif choice.isdigit() and 0 < int(choice) <= number_of_recipes:
            return ('see', int(choice)-1)

        print(f"The number must be between 1 and {number_of_recipes}!")

def display_recipe(recipe):
    newline = '\n'
    print(f"\nThe {recipe.get('name', 'UNKNOWN')}: {newline.join(recipe.get('description', ['NO DESCRIPTION']))}")
    print("\nTo make it you will need:")
    for ingredient in recipe.get('ingredients', []):
        print(f"\t{ingredient}")

def collect_recipe() -> dict:
    recipe = { 'description': [], 'ingredients': []}
    print("Adding a new recipe for: ", end='')
    name = input().strip()
    if not name: 
        return None
    recipe['name'] = name 
    while True: 
        description = input("description: ").strip()
        if not description:
            break 
        recipe['description'].append(description)
    while True: 
        ingredient = input("ingredient: ").strip()
        if not ingredient:
            break 
        recipe['ingredients'].append(ingredient)
    return recipe 

def save_changes(recipes: list):
    newline = '\n'
    with open(filename, 'w') as f: 
        if filename.endswith('rd1'):
            for recipe in recipes: 
                f.write(f"n: {recipe['name']}"+newline)
                for desc in recipe['description']: 
                    f.write(f"d: {desc}"+newline)
                for ingredient in recipe['ingredients']: 
                    f.write(f"i: {ingredient}"+newline)
        if filename.endswith('rd2'):
            for recipe in recipes: 
                f.write(f"{len(recipe['description'])} {len(recipe['ingredients'])} {recipe['name']}"+newline)
                for desc in recipe['description']: 
                    f.write(f"{desc}"+newline)
                for ingredient in recipe['ingredients']: 
                    f.write(f"{ingredient}"+newline)

def update_recipes_with(recipe: dict):
    while True:
        if recipe: 
            existing = next((r for r in recipes if r['name'] == recipe['name']), None)
            if existing:
                while True: 
                    print(f"We already have a recipe for '{recipe['name']}'. Do you want to replace it? (say 'yes' or 'no'): ")
                    choice = input().strip()
                    if choice == 'yes':
                        recipes.remove(existing)
                        break
                    elif choice == 'no':                     
                        newname = input("Save the new recipe as: ").strip()
                        if newname:
                            recipe['name'] = newname
                            break 
            else: 
                recipes.append(recipe)
                break

# the main application loop. keep going until it is time to end
while True: 
    display_recipes()
    (action, recipe_id) = get_users_choice(len(recipes))
    if action == 'exit': 
        if has_changes:
            while True: 
                choice = input('Do you want to save changes to recipes.rd1? (yes or no): ').strip()
                if choice == 'yes':
                    save_changes(recipes)
                    break
                elif choice == 'no':
                    break 
        print("\nThank your for cooking with Python. Goodbye.")
        break  
    if action == 'see':
        display_recipe(recipes[recipe_id])
    elif action == 'add':
        update_recipes_with(collect_recipe())
        has_changes = True 
        
    print("\n\nLet's try again!\n")