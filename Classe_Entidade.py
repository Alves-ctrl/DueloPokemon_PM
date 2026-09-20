from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, id=None):
        self.id = id

    @abstractmethod

    def __str__(self):
        pass
        
