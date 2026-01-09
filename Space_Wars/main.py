from funcoes import *
from tabuleiro import Tabuleiro

if __name__ == "__main__":
    naves = None
    tiros_total = 0
    tiros_certos = 0
    naves_posicoes = None
    tiros_posicoes = None

    while True:
        limpar_tela()
        mostrar_capa()
        opc = menu()

        if opc == "1":
            tab = Tabuleiro()
            naves, tiros_total, tiros_certos, naves_posicoes, tiros_posicoes = iniciar_jogo(
                tab, naves, tiros_total, tiros_certos, naves_posicoes, tiros_posicoes
            )
        elif opc == "2":
            dados = carregar_jogo_com_selecao()
            if dados:
                naves = criar_naves(dados)
                tiros_total = dados.get("tiros_total", 0)
                tiros_certos = dados.get("tiros_certos", 0)
                naves_posicoes = [tuple(pos) for pos in dados.get("naves_posicoes", [])]
                tiros_posicoes = [tuple(pos) for pos in dados.get("tiros_posicoes", [])]
                tab = Tabuleiro()
                naves, tiros_total, tiros_certos, naves_posicoes, tiros_posicoes = iniciar_jogo(
                    tab, naves, tiros_total, tiros_certos, naves_posicoes, tiros_posicoes
                )
        elif opc == "3":
            if naves:
                salvar_jogo_com_nome(naves, tiros_total, tiros_certos, naves_posicoes, tiros_posicoes)
            else:
                print("Nenhum jogo para salvar!")
                input("Pressione Enter para continuar...")
        elif opc == "4":
            break
