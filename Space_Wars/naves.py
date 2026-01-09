from colorama import Fore, Style, init

init(autoreset=True)

class NaveModelo:
    def __init__(self, denominacao, cor, perda_energia, simbolo):
        self.denominacao = denominacao
        self.cor = cor
        self.energia = 100
        self.perda_energia = perda_energia
        self.simbolo = simbolo
        self.tiros_acertados = 0

    def reduzir_energia(self):
        self.energia -= self.perda_energia
        if self.energia < 0:
            self.energia = 0
        return self.energia

    def energia_atual(self):
        return self.energia

    def to_dict(self):
        return {
            "denominacao": self.denominacao,
            "cor": self.cor,
            "energia": self.energia,
            "perda_energia": self.perda_energia,
            "simbolo": self.simbolo,
            "tiros_acertados": self.tiros_acertados
        }


class NaveComEnergiaExtra(NaveModelo):
    def __init__(self, denominacao, cor, perda_energia, simbolo, energia_extra):
        super().__init__(denominacao, cor, perda_energia, simbolo)
        self.energia_extra = energia_extra

    def mostrar_dados(self):
        cor_texto = self._cor_terminal()
        print(f"{cor_texto}Nave: {self.denominacao} | Energia: {self.energia} | Símbolo: {self.simbolo}{Style.RESET_ALL}")

    def adicionar_energia_extra(self):
        self.energia += self.energia_extra
        if self.energia > 100:
            self.energia = 100
        return self.energia

    def _cor_terminal(self):
        cores = {
            'vermelha': Fore.RED,
            'azul': Fore.BLUE,
            'verde': Fore.GREEN,
            'amarela': Fore.YELLOW,
            'ciano': Fore.CYAN,
            'magenta': Fore.MAGENTA,
            'branca': Fore.WHITE
        }
        return cores.get(self.cor.lower(), Fore.WHITE)
