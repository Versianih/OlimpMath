from functions.functions import(
    acaoInvalida, voltar, get_keypress, clean, tratErro,
    GREEN, RED, CYAN, GRENN_BACKGROUND, RESET, WHITE
)

import functions.functions

def settings():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> CONFIGURAÇÔES:" + RESET)
        print("")
        print(CYAN + "1) Saída de Casas Decimais: " + GREEN  + str(functions.functions.casas_decimais), "casas decimais" + RESET)
        print(CYAN + "2) Saída - Unidade de Medida de Ângulos: " + GREEN +  str(functions.functions.saida_angulo) + RESET)
        print(CYAN + "3) Entrada - Unidade de Medida de Ângulos: " + GREEN +  str(functions.functions.entrada_angulo) + RESET)
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?:")
        escolha = get_keypress()

        if escolha == "1":
            clean()
            print(GREEN + "TELA INICIAL -> CONFIGURAÇÔES:" + RESET)
            print("")
            print(GRENN_BACKGROUND + WHITE + "1) Saída de Casas Decimais: " + str(functions.functions.casas_decimais), "casas decimais" + RESET)
            print(CYAN + "2) Saída - Unidade de Medida de Ângulos: " + GREEN +  str(functions.functions.saida_angulo) + RESET)
            print(CYAN + "3) Entrada - Unidade de Medida de Ângulos: " + GREEN +  str(functions.functions.entrada_angulo) + RESET)
            print("")
            preTratDecimais = input(CYAN + "Casas decimais atual: " + GREEN +  str(functions.functions.casas_decimais) + CYAN +  " Saída Nova:" + RESET)
            if tratErro(int, [preTratDecimais]) == True:
                functions.functions.casas_decimais = int(preTratDecimais)
            else:
                voltar()

        elif escolha == "2":
            saidaÂngulo()

        elif escolha == "3":
            entradaAngulo()
            
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def saidaÂngulo():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> CONFIGURAÇÔES:" + RESET)
        print("")
        print(CYAN + "1) Saída de Casas Decimais: " + GREEN  + str(functions.functions.casas_decimais), "casas decimais" + RESET)
        print(GRENN_BACKGROUND + WHITE + "2) Saída - Unidade de Medida de Ângulos: " +  str(functions.functions.saida_angulo) + RESET)
        print(GREEN + "   1) Graus" + RESET)
        print(GREEN + "   2) Radianos" + RESET)
        print(CYAN + "3) Entrada - Unidade de Medida de Ângulos: " + GREEN +  str(functions.functions.entrada_angulo) + RESET)
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?:")
        escolha = get_keypress()

        if escolha == "1":
            functions.functions.saida_angulo = "graus"
            break
        
        elif escolha == "2":
            functions.functions.saida_angulo = "rad"
            break

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def entradaAngulo():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> CONFIGURAÇÔES:" + RESET)
        print("")
        print(CYAN + "1) Saída de Casas Decimais: " + GREEN  + str(functions.functions.casas_decimais), "casas decimais" + RESET)
        print(CYAN + "2) Saída - Unidade de Medida de Ângulos: " + GREEN +  str(functions.functions.saida_angulo) + RESET)
        print(GRENN_BACKGROUND + WHITE + "3) Entrada - Unidade de Medida de Ângulos: " +  str(functions.functions.entrada_angulo) + RESET)
        print(GREEN + "   1) Graus" + RESET)
        print(GREEN + "   2) Radianos" + RESET)
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?:")
        escolha = get_keypress()

        if escolha == "1":
            functions.functions.entrada_angulo = "graus"
            break

        elif escolha == "2":
            functions.functions.entrada_angulo = "rad"
            break

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()