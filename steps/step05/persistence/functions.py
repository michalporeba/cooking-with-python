import os.path 
from .RecipeStore import RecipeStore 
from .Rd1 import Rd1
from .Rd2 import Rd2 

def read_from(connection: str) -> list: 
    store = __get_store(connection)
    with open(connection) as f: 
        return store.read_all(f)
    
def write_to(connection: str, recipes: list):
    store = __get_store(connection)
    with open(connection, 'w') as f:
        store.save_all(f, recipes)


def __get_store(connection: str) -> RecipeStore: 
    if not os.path.isfile(connection):
        raise FileNotFoundError(connection)
    if connection.endswith('.rd1'):
        return Rd1()
    if connection.endswith('.rd2'):
        return Rd2()
    