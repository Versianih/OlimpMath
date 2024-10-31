from functions.functions import (
    clean, get_keypress, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from views.geoView.geoPlanaView import geometriaPlana
from views.geoView.geoEspacialView import geometriaEspacial
from views.geoView.geoAnaliticaView import geometriaAnalítica


def geometria():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA")
        print(YELLOW + "1) Geometria Plana")
        print("2) Geometria Espacial")
        print("3) Geometria Analítica")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()
        
        # Geometria Plana
        if escolha == "1":
            geometriaPlana()

        # Geometria Espacial
        elif escolha == "2":
            geometriaEspacial()

        # Geometria Analítica
        elif escolha == "3":
            geometriaAnalítica()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()