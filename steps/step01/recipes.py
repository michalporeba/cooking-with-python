# the data - for now hardcoded three recipes
recipes = [
    { 'name': "lemon cake", 'description': "a cake with a lemon"},
    { 'name': "brownie", 'description': "a simple cake with chocolate"},
    { 'name': "cookie"} # there is no description, so we can test this behaviour
]

def display_recipes():
    print("Available recipes:")
    for i, recipe in enumerate(recipes):
        print(f"\t{i+1} - {recipe['name']}")

def get_users_choice(number_of_recipes) -> int: 
    while True:
        print("\n(choose recipe number, or press enter to exit)")
        choice = input("which recipe would you like to see?\n")
        if not choice:
            return None
        elif choice.isdigit() and 0 < int(choice) <= number_of_recipes:
            return int(choice)

        print(f"The number must be between 1 and {number_of_recipes}!")

def display_recipe(recipe):
    print(f"\n{recipe.get('name', 'UNKNOWN')}: {recipe.get('description', 'NO DESCRIPTION')}")


# the main application loop. keep going until it is time to end
while True: 
    display_recipes()
    choice = get_users_choice(len(recipes))
    if not choice: # there is no choice, so it is time to stop
        break; 
    
    display_recipe(recipes[choice-1])
    print("\n\nLet's try again!\n")


