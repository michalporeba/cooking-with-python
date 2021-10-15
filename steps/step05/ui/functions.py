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

def display_recipe(recipe):
    newline = '\n'
    print(f"\nThe {recipe.get('name', 'UNKNOWN')}: {newline.join(recipe.get('description', ['NO DESCRIPTION']))}")
    print("\nTo make it you will need:")
    for ingredient in recipe.get('ingredients', []):
        print(f"\t{ingredient}")

def display_recipes(recipes: list):
    print("Available recipes:")
    for i, recipe in enumerate(recipes):
        print(f"\t{i+1} - {recipe['name']}")