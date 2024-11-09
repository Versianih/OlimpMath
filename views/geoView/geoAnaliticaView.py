from functions.functions import (
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from functions.geoFunctions.geoAnalitica import (
    distPontos,
)


def geometriaAnalítica():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA ANALÍTICA")
        print(YELLOW + "1) Distância entre dois pontos")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        if escolha == "1":
            clean()
            distPontos(input("Xa:"), input("Ya:"), input("Xb:"), input("Yb:"), True)
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()