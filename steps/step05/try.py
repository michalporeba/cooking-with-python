def do(actions):
    for i, (k,v) in enumerate(actions.items()): 
        print(f"{i+1}) {k}")

do({
    'Option 1': lambda : print('a'),
    'Option 2': lambda : print('b')
})