import pickle
from pokemon import Entidade

class EntidadeDAO:
    _instancias = {}

    @classmethod
    def get_instancia(cls, tipo_entidade):
        if tipo_entidade not in cls._instancias:
            cls._instancias[tipo_entidade] = cls(tipo_entidade)
        return cls._instancias[tipo_entidade]

    def __init__(self, tipo_entidade):
        self.tipo_entidade = tipo_entidade
        self.elementos = set()
        self.arquivo = f"dados_{tipo_entidade.__name__.lower()}.pkl"

    def salvar(self, objeto: Entidade) -> bool:
        if any(e.id == objeto.id for e in self.elementos):
            return False
        self.elementos.add(objeto)
        return True

    def atualizar(self, objeto: Entidade) -> bool:
        existente = self.buscar(objeto.id)
        if existente:
            self.elementos.remove(existente)
            self.elementos.add(objeto)
            return True
        return False

    def apagar(self, id_entidade: int):
        existente = self.buscar(id_entidade)
        if existente:
            self.elementos.remove(existente)
            return existente
        return None

    def buscar(self, id_entidade: int):
        for elemento in self.elementos:
            if elemento.id == id_entidade:
                return elemento
        return None

    def carregar(self) -> list:
        return sorted(list(self.elementos), key=lambda x: x.id) 

    def persistir(self):
        with open(self.arquivo, 'wb') as f:
            pickle.dump(self.elementos, f)

    def recuperar(self):
        try:
            with open(self.arquivo, 'rb') as f:
                self.elementos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.elementos = set()
