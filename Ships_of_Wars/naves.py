# Nave.py

class NaveModelos:
    def __init__(self, denominacaoNave, corNave, perdaEnergia, simbolo):
        self.__denominacaoNave = denominacaoNave # Privado
        self.__corNave = corNave # Privado
        self.__energia = 100 # Inicia sempre em 100
        self.__perdaEnergia = perdaEnergia # Privado
        self.__simbolo = simbolo # Privado
        
    #Getters e Setters para denominacaoNave
    @property
    def denominacaoNave(self):
        return self.__denominacaoNave

    @denominacaoNave.setter
    def denominacaoNave(self, valor):
        self.__denominacaoNave = valor
        
    #Getters e Setters para corNave
    @property
    def corNave(self):
        return self.__corNave

    @corNave.setter
    def corNave(self, valor):
        self.__corNave = valor
        
    #Getters e Setters para energia
    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        self.__energia = valor
        
    #Getters e Setters para perdaEnergia
    @property
    def perdaEnergia(self):
        return self.__perdaEnergia

    @perdaEnergia.setter
    def perdaEnergia(self, valor):
        self.__perdaEnergia = valor
        
    #Getters e Setters para simbolo
    @property
    def simbolo(self):
        return self.__simbolo

    @simbolo.setter
    def simbolo(self, valor):
        self.__simbolo = valor
        
     # método para perder energia
    def perder_energia(self):
        self.__energia -= self.__perdaEnergia
        if self.__energia < 0:
            self.__energia = 0
        return self.__energia
    
class NaveEspacial(NaveModelos):
    def __init__(self, denominacao, cor, perda_energia, simbolo, energiaExtra):
        super().__init__(denominacao, cor, perda_energia, simbolo)
        self.__energiaExtra = energiaExtra  # Privado
        
    #Getters e Setters para energiaExtra
    @property
    def energiaExtra(self):
        return self.__energiaExtra

    @energiaExtra.setter
    def energiaExtra(self, valor):
        self.__energiaExtra = valor
        
    # Método para mostrar dados da nave com cor
    def mostrar_dados(self):
        # apenas uma simulação de cores no terminal
        cores_terminal = {
            "vermelho": "\033[91m",
            "verde": "\033[92m",
            "amarelo": "\033[93m",
            "azul": "\033[94m",
            "reset": "\033[0m"
        }
        cor_esc = cores_terminal.get(self.corNave.lower(), cores_terminal["reset"])
        print(f"{cor_esc}Nave: {self.denominacaoNave} | Energia: {self.energia} | Símbolo: {self.simbolo}{cores_terminal['reset']}")

    # Método para adicionar energia extra sem ultrapassar 100
    def adicionar_energia_extra(self):
        self._NaveModelo__energia += self.__energiaExtra  # acessando atributo privado da classe base
        if self.energia > 100:
            self._NaveModelo__energia = 100
        return self.energia
        
    
