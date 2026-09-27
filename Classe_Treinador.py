from Classe_Entidade import Entidade
#JA ALTERADA
class Treinador(Entidade):
    def __init__(self, id=None, nome = ""):
        super().__init__(id)

        self.nome = nome
        self.times = []

    def __str__(self):
        return(
            f"Treinador [{super().__str__()}, "
            f"Nome: {self.nome}, "
            f"Quantidade de times: {len(self.times)}]"
        )

    def addTime(self,time):
        if time == None:
            return False
        #se o time for vazio
        if self.buscarTime(time.id) is not None:
            return False
        #se tiver um time com o mesmo id
        if time.treinador is not self:
            return False
        #se nao for do treinador certo

        self.times.append(time)
        #adiciona o time na lista de times do treinador
    
    def removeTime(self, id_time):
        time = self.buscarTime(id_time)

        if time == None:
            return False
        #verifica se o existe

        self.time.remove(time)
        return True

    def buscarTime(self, id_time):
        for time in self.times:
            if time.id == id_time:
                #procura no vetor times um id igual
                return time
        return None

    def listTime(self):
        return self.times.copy()
        #retorna uma copia do vetor times, essa copia nao permite alterar os objetos originais
        
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
