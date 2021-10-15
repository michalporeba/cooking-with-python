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
                recipe = { 'name': value, 'description': '', 'ingredients': [] }
                recipes.append(recipe)
        elif key == 'd':
            if recipe['description']:
                recipe['description'] += "\n"
            recipe['description'] += value
        elif key == 'i':
            recipe['ingredients'].append(value)
        
def display_recipes():
    print("Available recipes:")
    for i, recipe in enumerate(recipes):
        print(f"\t{i+1} - {recipe['name']}")

def get_users_choice(number_of_recipes: int) -> int: 
    while True:
        print("\n(choose recipe number, or press enter to exit)")
        choice = input("which recipe would you like to see?\n")
        if not choice:
            return None
        elif choice.isdigit() and 0 < int(choice) <= number_of_recipes:
            return int(choice)

        print(f"The number must be between 1 and {number_of_recipes}!")

def display_recipe(recipe):
    print(f"\nThe {recipe.get('name', 'UNKNOWN')}: {recipe.get('description', 'NO DESCRIPTION')}")
    print("\nTo make it you will need:")
    for ingredient in recipe.get('ingredients', []):
        print(f"\t{ingredient}")

# the main application loop. keep going until it is time to end
while True: 
    display_recipes()
    choice = get_users_choice(len(recipes))
    if not choice: # there is no choice, so it is time to stop
        print("\nThank your for using cooking with Python. Boodbye.")
        break; 
    
    display_recipe(recipes[choice-1])
    print("\n\nLet's try again!\n")


