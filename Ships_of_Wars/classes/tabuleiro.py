import random

class Tabuleiro:
    def __init__(self, x=10, y=10, fill='.'):

        # Cria um tabuleiro com dimensões x (linhas) e y (colunas)
        # fill: caractere para preencher o tabuleiro
        self.x = x
        self.y = y
        self.fill = fill
        self.matriz = [[self.fill for _ in range(self.y)] for _ in range(self.x)]

    def imprimir(self):
        """Imprime a matriz atual do tabuleiro"""
        for linha in self.matriz:
            print(' '.join(linha))

    def criar_matriz(self):
        """Gera uma matriz limpa"""
        self.matriz = [[self.fill for _ in range(self.y)] for _ in range(self.x)]

    def posicao_valida(self, i, j):
        """Verifica se a posição (i,j) está dentro do tabuleiro"""
        return 0 <= i < self.x and 0 <= j < self.y

    def posicao_aleatoria_sem_choque(self, ocupadas):
        """Retorna uma posição aleatória que não esteja ocupada"""
        while True:
            i = random.randint(0, self.x - 1)
            j = random.randint(0, self.y - 1)
            if (i, j) not in ocupadas:
                return (i, j)
