import sys
from persistence import functions as pf
from ui import functions as ui

recipes = []
has_changes = False
filename = 'recipes.rd1'

if (len(sys.argv)>1):
    filename = sys.argv[1]

recipes = pf.read_from(filename)

def do(prompt, actions):
    options = ", ".join(actions.keys())
    while True: 
        print(f"{prompt} ({options}): ", end='')
        choice = input()
        action = next(iter([v for k,v in actions.items() if k == choice] +  
            [v for k,v in actions.items() if choice and k.startswith(choice)]), None)
        if action:
            action()
            break

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
    ui.display_recipes(recipes)
    (action, recipe_id) = get_users_choice(len(recipes))
    if action == 'exit': 
        if has_changes:
            while True: 
                choice = input('Do you want to save changes to recipes.rd1? (yes or no): ').strip()
                if choice == 'yes':
                    pf.write_to(filename, recipes)
                    break
                elif choice == 'no':
                    break 
        print("\nThank your for cooking with Python. Goodbye.")
        break  
    if action == 'see':
        ui.display_recipe(recipes[recipe_id])
    elif action == 'add':
        update_recipes_with(ui.collect_recipe())
        has_changes = True 
        
    print("\n\nLet's try again!\n")