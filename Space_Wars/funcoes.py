import os
import json
import random
from naves import NaveComEnergiaExtra

# ----------------------- UTILITÁRIOS -----------------------
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_capa():
    print("===================================")
    print("          JOGO DAS NAVES           ")
    print("===================================")

def menu():
    print("\nMenu:")
    print("1 - Iniciar Jogo")
    print("2 - Carregar Jogo")
    print("3 - Guardar Jogo")
    print("4 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

# ----------------------- NAVE -----------------------
def criar_naves(dados=None):
    if dados:
        naves = []
        for d in dados["naves"]:
            nave = NaveComEnergiaExtra(d["denominacao"], d["cor"], d["perda_energia"], d["simbolo"], 20)
            nave.energia = d["energia"]
            nave.tiros_acertados = d.get("tiros_acertados", 0)
            naves.append(nave)
        return naves
    else:
        return [
            NaveComEnergiaExtra("Falcão", "vermelha", 10, "F", 20),
            NaveComEnergiaExtra("Águia", "azul", 15, "A", 15),
            NaveComEnergiaExtra("Corvo", "verde", 20, "C", 10)
        ]

def atualizar_energia_naves(naves, tiros_posicoes, naves_posicoes):
    acertos = 0
    for idx, nave in enumerate(naves):
        if naves_posicoes[idx] in tiros_posicoes and nave.energia > 0:
            nave.reduzir_energia()
            nave.tiros_acertados += 1
            acertos += 1
    return acertos

# ----------------------- JOGO -----------------------
def iniciar_jogo(tabuleiro, naves=None, tiros_total=0, tiros_certos=0, naves_posicoes=None, tiros_posicoes=None):
    from tabuleiro import Tabuleiro
    limpar_tela()
    mostrar_capa()

    if naves is None:
        naves = criar_naves()

    tab = tabuleiro
    tab.limpar()
    tab.posicionar_naves(naves)
    if naves_posicoes:
        tab.naves_posicoes = naves_posicoes
    if tiros_posicoes:
        tab.tiros_posicoes = tiros_posicoes

    # Pergunta ao jogador se quer jogar manualmente ou automático
    while True:
        modo = input("Deseja jogar manualmente (M) ou automaticamente (A)? ").strip().upper()
        if modo in ["M", "A"]:
            break

    while tiros_total < 105 and any(n.energia > 0 for n in naves):
        limpar_tela()

        # Limpar tiros da rodada anterior antes de gerar os novos
        tab.tiros_posicoes = []

        # Mostrar tabuleiro com naves ocultas
        print("Tabuleiro (naves ocultas):")
        tab.mostrar(mostrar_naves=False)

        # Verificar se o jogador quer sair
        sair = input("Pressione 'S' para sair do jogo ou Enter para continuar: ").strip().upper()
        if sair == "S":
            # Perguntar se quer salvar antes de sair
            salvar = input("Deseja salvar o jogo antes de sair? (S/N): ").strip().upper()
            if salvar == "S":
                salvar_jogo("save.json", naves, tiros_total, tiros_certos, tab.naves_posicoes, tab.tiros_posicoes)
            print("Saindo do jogo e voltando ao menu...")
            break

        # Definir os tiros
        tiros = []
        if modo == "A":
            tiros = tab.gerar_tiros_aleatorios(3)
            print(f"Tiros automáticos: {tiros}")
        else:  # Modo manual
            for _ in range(3):
                while True:
                    try:
                        x = int(input(f"Digite a linha do tiro (0-{tab.tamanho-1}): "))
                        y = int(input(f"Digite a coluna do tiro (0-{tab.tamanho-1}): "))
                        if (x,y) not in tab.tiros_posicoes and 0 <= x < tab.tamanho and 0 <= y < tab.tamanho:
                            tiros.append((x,y))
                            tab.tiros_posicoes.append((x,y))
                            break
                        else:
                            print("Posição inválida ou já atingida. Tente novamente.")
                    except ValueError:
                        print("Digite números válidos.")

        tiros_total += 3

        acertos = atualizar_energia_naves(naves, tiros, tab.naves_posicoes)
        tiros_certos += acertos

        # Mostrar apenas tiros da rodada atual
        print("\nTabuleiro dos Tiros:")
        tab.mostrar(mostrar_naves=False)

        print("Dados das Naves (somente energia atual, sem revelar posições):")
        for n in naves:
            n.mostrar_dados()

        eficacia = (tiros_certos * 100 / tiros_total) if tiros_total > 0 else 0
        print(f"Tiros totais: {tiros_total} | Tiros certeiros: {tiros_certos} | Eficácia: {eficacia:.2f}%")

        # Adicionar energia extra após 45 tiros
        if tiros_total == 45:
            for n in naves:
                n.adicionar_energia_extra()
                print(f"{n.denominacao} recebeu energia extra!")

        input("\nPressione Enter para continuar...")

    print("\nFim do jogo!")
    return naves, tiros_total, tiros_certos, tab.naves_posicoes, tab.tiros_posicoes





# ----------------------- SALVAR / CARREGAR -----------------------
def salvar_jogo_com_nome(naves, tiros_total, tiros_certos, naves_posicoes, tiros_posicoes):
    nome = input("Digite o nome para salvar o jogo: ").strip()
    if not nome:
        print("Nome inválido! Salvando como 'save.json' por padrão.")
        nome = "save"
    arquivo = f"{nome}.json"
    
    dados = {
        "naves": [n.to_dict() for n in naves],
        "tiros_total": tiros_total,
        "tiros_certos": tiros_certos,
        "naves_posicoes": naves_posicoes,
        "tiros_posicoes": tiros_posicoes
    }
    with open(arquivo, "w") as f:
        json.dump(dados, f)
    print(f"Jogo salvo com sucesso como '{arquivo}'!")
    
import glob

def listar_jogos_salvos():
    arquivos = glob.glob("*.json")
    if not arquivos:
        print("Nenhum jogo salvo encontrado.")
        return []
    print("\nJogos salvos disponíveis:")
    for i, arq in enumerate(arquivos):
        print(f"{i+1} - {arq}")
    return arquivos

def carregar_jogo_com_selecao():
    arquivos = listar_jogos_salvos()
    if not arquivos:
        return None
    while True:
        try:
            escolha = int(input("Digite o número do jogo que deseja carregar: "))
            if 1 <= escolha <= len(arquivos):
                arquivo = arquivos[escolha-1]
                with open(arquivo, "r") as f:
                    dados = json.load(f)
                print(f"Jogo '{arquivo}' carregado com sucesso!")
                return dados
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def carregar_jogo(arquivo):
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
        return dados
    except FileNotFoundError:
        print("Arquivo de salvamento não encontrado.")
        return None
