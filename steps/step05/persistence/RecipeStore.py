from abc import abstractmethod
import io 

class RecipeStore():
    @abstractmethod
    def read_all(self, file: io.TextIOWrapper) -> list:
        raise NotImplementedError
    @abstractmethod
    def save_all(self, file: io.TextIOWrapper, recipes: list):
        raise NotImplementedError