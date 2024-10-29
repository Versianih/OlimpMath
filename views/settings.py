from functions.functions import(
    acaoInvalida, voltar, get_keypress, clean,
    GREEN, RED, CYAN, RESET
)

def settings():
    casas_decimais = 2
    saida_angulo = "Graus"
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> CONFIGURAÇÔES:" + RESET)
        print("")
        print(CYAN + "1) Saída de Casas Decimais: " + GREEN  + str(casas_decimais), "casas decimais" + RESET)
        print(CYAN + "2) Unidade de Medida de Ângulos: " + GREEN +  str(saida_angulo) + RESET)
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?:")
        escolha = get_keypress()

        if escolha == "1":
            clean()
            casas_decimais = int(input(CYAN + "Casas decimais atual: " + GREEN +  str(casas_decimais) + CYAN +  " Saída Nova:" + RESET))
            print(GREEN + "Sucesso! " + CYAN + "A saída de casas decimais agora é de: " + GREEN +  str(casas_decimais), "casas decimais" + RESET)
            voltar()

        elif escolha == "2":
            print("Função de alterar saída de unidade de medida de angulos ainda não pronta")
            input()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()

def saidaÂngulo():
    while True:
        break