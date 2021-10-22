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



do('Choose what you want', {
    'yes': lambda : print('yes was selected'),
    'no': lambda : print('no was selected')
})


