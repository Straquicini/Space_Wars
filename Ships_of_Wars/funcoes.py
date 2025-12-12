# funcoes.py
# Contém funções gerais do jogo: desenho do tabuleiro, colocação aleatória, salvar/carregar, etc.

import random
import json
import os
from classes.naves import NaveModelo as NM, NaveEspacial as NE
from classes.tabuleiro import Tabuleiro as T

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
            n = NE.from_dict(nd)
        else:
            n = NE.from_dict(nd)
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
    if not T.posicao_valida(n_linhas, n_colunas, x, y):
        return False, 'Coordenadas fora do tabuleiro.'
    if (x,y) in tiros_existentes:
        return False, 'Já foi dado um tiro nessa casa.'
    return True, ''