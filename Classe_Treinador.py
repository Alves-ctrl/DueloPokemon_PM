
class Treinador:

    def __init__(self, id=None, nome=""):
        self.id = id
        self.nome = nome
        self.times = []

    def __str__(self):
        return (
            f"Treinador [ID: {self.id}, "
            f"Nome: {self.nome}, "
            f"Quantidade de times: {len(self.times)}]"
        )

    def addTime(self, time):
        if time is None:
            return False

        if time.treinador is not self:
            return False

        if self.buscarTime(time.id) is not None:
            return False

        self.times.append(time)
        return True

    def removerTime(self, id_time):
        time = self.buscarTime(id_time)

        if time is None:
            return False

        self.times.remove(time)
        return True

    def buscarTime(self, id_time):
        for time in self.times:
            if time.id == id_time:
                return time

        return None

    def listarTimes(self):
        return self.times.copy()


'''
A classe Treinador representa um jogador e gerencia os times que pertencem a ele. Ela não executa ataques, não controla rodadas e não modifica os atributos dos Pokémon.
Atributos:

-id,int	
Identificador herdado de Entidade.

-nome,str	
Nome do treinador.

-times,list[Time]	
Times cadastrados pelo treinador.
O atributo times será uma lista de objetos Time, e não uma lista de Pokémon. Cada time será responsável por administrar seus próprios Pokémon.

Métodos:

__init__(id=None, nome="")
Inicializa o treinador e sua lista de times.

__str__()	
Retorna o ID, o nome e a quantidade de times.

adicionarTime(time)	
Associa um time ao treinador.

removerTime(id_time)	
Remove a associação com um time.

buscarTime(id_time)	
Busca um dos times do treinador pelo ID.

listarTimes()	
Retorna os times pertencentes ao treinador.

O construtor utilizará super().__init__(id) e o método __str__() utilizará super().__str__().
'''
