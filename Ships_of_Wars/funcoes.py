# funcoes.py
# Contém funções gerais do jogo: desenho do tabuleiro, colocação aleatória, salvar/carregar, etc.

import random
import json
import os
from naves import NaveModelo, NaveExtra

# Mapas de cores ANSI simples (só cores básicas portáteis)
ANSI_COLORS = {
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'reset': '\u001b[0m'
}


def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_matriz(n=10, m=10, fill='.'):
    return [[fill for _ in range(m)] for _ in range(n)]


def imprimir_matriz(mat):
    for linha in mat:
        print(' '.join(linha))


def marcar_naves_no_tabuleiro(mat, posicoes, mostrar_mortas=False):
    # posicoes: dict -> nome_nave: (x,y, objeto_nave)
    matriz = [row[:] for row in mat]
    for chave, (x, y, nave) in posicoes.items():
        if nave.energia > 0 or mostrar_mortas:
            cor_code = ANSI_COLORS.get(nave.cor, '')
            reset = ANSI_COLORS['reset']
            matriz[x][y] = f"{cor_code}{nave.simbolo}{reset}"
        else:
            matriz[x][y] = '.'
    return matriz


def marcar_tiros_no_tabuleiro(mat, tiros):
    matriz = [row[:] for row in mat]
    for (x, y) in tiros:
        matriz[x][y] = 'X'
    return matriz


def posicao_valida(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


def posicao_aleatoria_sem_choque(n, m, ocupadas):
    # ocupadas: set of (x,y)
    while True:
        x = random.randint(0, n-1)
        y = random.randint(0, m-1)
        if (x,y) not in ocupadas:
            return (x,y)


def salvar_jogo(filepath, estado):
    # estado deve ser serializável: converter objetos
    serial = {}
    serial['naves'] = {k: v.to_dict() for k,v in estado['naves_obj'].items()}
    serial['posicoes'] = {k: [pos[0], pos[1]] for k,pos in estado['posicoes'].items()}
    serial['tiros'] = [[x,y] for x,y in estado['tiros']]
    serial['total_tiros'] = estado['total_tiros']
    serial['total_acertos'] = estado['total_acertos']
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(serial, f, indent=2, ensure_ascii=False)


def carregar_jogo(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    naves_obj = {}
    for nome, nd in data['naves'].items():
        if nd.get('classe') == 'NaveExtra':
            n = NaveExtra.from_dict(nd)
        else:
            n = NaveModelo.from_dict(nd)
        naves_obj[nome] = n
    posicoes = {nome: (p[0], p[1], naves_obj[nome]) for nome, p in data['posicoes'].items()}
    tiros = [tuple(t) for t in data['tiros']]
    estado = {
        'naves_obj': naves_obj,
        'posicoes': posicoes,
        'tiros': tiros,
        'total_tiros': data.get('total_tiros', 0),
        'total_acertos': data.get('total_acertos', 0)
    }
    return estado


def calcular_eficacia(total_tiros, total_acertos):
    if total_tiros == 0:
        return 0.0
    return (total_acertos * 100.0) / total_tiros


def colocar_naves_aleatoriamente(n_linhas, n_colunas, naves_obj):
    ocupadas = set()
    posicoes = {}
    for nome, nave in naves_obj.items():
        x,y = posicao_aleatoria_sem_choque(n_linhas, n_colunas, ocupadas)
        ocupadas.add((x,y))
        posicoes[nome] = (x,y,nave)
    return posicoes


def validar_e_adicionar_tiro(n_linhas, n_colunas, tiros_existentes, x, y):
    if not posicao_valida(n_linhas, n_colunas, x, y):
        return False, 'Coordenadas fora do tabuleiro.'
    if (x,y) in tiros_existentes:
        return False, 'Já foi dado um tiro nessa casa.'
    return True, ''