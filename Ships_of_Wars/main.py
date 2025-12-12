from funcoes import salvar_jogo as SJ, carregar_jogo as CJ, mostrar_capa as MC, menu_principal as MP, criar_naves as CN, colocar_naves_aleatoriamente as CNA, \
validar_e_adicionar_tiro as VAT, aplicar_tiros as AT, atualizar_tabuleiro as ATT, limpar_ecra as LE, pausar as P
from classes.naves import NaveModelo as NM, NaveEspacial as NE
from classes.tabuleiro import Tabuleiro as T

tab = T(x=10, y=10)
tab.criar_matriz()

def main():
    """
    Método único para iniciar o jogo completo.
    Inclui menu, rounds de tiros, atualização de energia, estatísticas, salvar/carregar.
    """
    MC()
    while True:
        escolha = MP()
        
        if escolha == "1":  # Iniciar Jogo
            naves = CN()
            tab = T(10, 10)
            posicoes = CNA(tab, naves)
            tiros = []
            total_tiros = 0
            total_acertos = 0

            # Loop principal do jogo
            while total_tiros < 105 and any(nave.energia > 0 for nave in naves.values()):
                LE()
                print(f"Round {total_tiros // 3 + 1}")

                # Inserir 3 tiros aleatórios
                novos_tiros = [VAT(tab, tiros) for _ in range(3)]
                tiros.extend(novos_tiros)
                total_tiros += 3

                # Aplicar tiros nas naves
                acertos = AT(posicoes, novos_tiros)
                total_acertos += acertos

                # Energia extra após 45 tiros
                if total_tiros == 45:
                    for nave in naves.values():
                        if nave.energia > 0 and hasattr(nave, "adicionar_energia_extra"):
                            nave.adicionar_energia_extra()

                # Atualizar tabuleiros
                ATT(tab, posicoes, tiros)

                # Mostrar tabuleiros
                print("\nTabuleiro com Naves:")
                tab.imprimir()

                print("\nTabuleiro com Tiros:")
                temp_tab = T(tab.x, tab.y)
                temp_tab.marcar_tiros(tiros)
                temp_tab.imprimir()

                # Mostrar dados das naves
                print("\nDados das naves:")
                for nave in naves.values():
                    if hasattr(nave, "mostrar_dados"):
                        nave.mostrar_dados()
                    else:
                        print(f"Nave: {nave.denominacao} | Energia: {nave.energia} | Símbolo: {nave.simbolo}")

                # Estatísticas
                eficacia = (total_acertos * 100 / total_tiros) if total_tiros > 0 else 0
                print(f"\nTotal de tiros: {total_tiros}")
                print(f"Total de acertos: {total_acertos}")
                print(f"Eficácia: {eficacia:.2f}%\n")

                P()

            # Fim do jogo
            LE()
            print("Fim do jogo!")
            if all(nave.energia <= 0 for nave in naves.values()):
                print("Todas as naves foram aniquiladas!")
            else:
                print("Número máximo de tiros atingido!")

        elif escolha == "2":  # Carregar Jogo
            try:
                estado = CJ("jogo.json")
                naves = estado['naves_obj']
                posicoes = estado['posicoes']
                tiros = estado['tiros']
                tab = T(10, 10)
                ATT(tab, posicoes, tiros)
                tab.imprimir()
                P()
            except FileNotFoundError:
                print("Nenhum jogo salvo encontrado.")
                P()

        elif escolha == "3":  # Guardar Jogo
            try:
                estado = {
                    'naves_obj': naves,
                    'posicoes': posicoes,
                    'tiros': tiros,
                    'total_tiros': total_tiros,
                    'total_acertos': total_acertos
                }
                SJ("jogo.json", estado)
                print("Jogo salvo com sucesso!")
                P()
            except NameError:
                print("Nenhum jogo em andamento para salvar.")
                P()

        elif escolha == "4":  # Sair
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")
            P()


if __name__ == "__main__":
    main()
