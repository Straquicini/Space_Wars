import random

class Tabuleiro:
    def __init__(self, tamanho=5):
        self.tamanho = tamanho
        self.matriz = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
        self.naves_posicoes = []
        self.tiros_posicoes = []

    def limpar(self):
        self.matriz = [[" " for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.tiros_posicoes = []

    def posicionar_naves(self, naves):
        self.naves_posicoes = []
        for nave in naves:
            while True:
                x = random.randint(0, self.tamanho - 1)
                y = random.randint(0, self.tamanho - 1)
                if (x, y) not in self.naves_posicoes:
                    self.matriz[x][y] = nave.simbolo
                    self.naves_posicoes.append((x, y))
                    break

    def registrar_tiros(self, tiros):
        for tiro in tiros:
            if tiro not in self.tiros_posicoes:
                self.tiros_posicoes.append(tiro)

    def gerar_tiros_aleatorios(self, quantidade=3):
        tiros = []
        while len(tiros) < quantidade:
            x = random.randint(0, self.tamanho - 1)
            y = random.randint(0, self.tamanho - 1)
            if (x, y) not in self.tiros_posicoes:
                tiros.append((x, y))
                self.tiros_posicoes.append((x, y))
        return tiros

    def remover_nave(self, posicao):
        if posicao in self.naves_posicoes:
            x, y = posicao
            self.matriz[x][y] = " "
            self.naves_posicoes.remove(posicao)

    def mostrar(self, mostrar_naves=True):
        for i in range(self.tamanho):
            linha = []
            for j in range(self.tamanho):
                if (i,j) in self.tiros_posicoes:
                    linha.append("X")
                elif mostrar_naves and (i,j) in self.naves_posicoes:
                    linha.append(self.matriz[i][j])
                else:
                    linha.append(" ")
            print(" | ".join(linha))
        print()
