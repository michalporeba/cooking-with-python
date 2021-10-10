recipes = []

with open('recipes.rd1') as f: 
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

# the main application loop. keep going until it is time to end
while True: 
    display_recipes()
    (action, recipe_id) = get_users_choice(len(recipes))
    if action == 'exit': 
        print("\nThank your for cooking with Python. Goodbye.")
        break  
    if action == 'see':
        display_recipe(recipes[recipe_id])
    elif action == 'add':
        recipe = collect_recipe()
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
    print("\n\nLet's try again!\n")
