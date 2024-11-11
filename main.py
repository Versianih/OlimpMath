# Telas
from views.geoView.geoView import geometria
from views.baseView import base
from views.algebraView import algebra
from views.combinatoriaView import combinatoria
from views.trigView import trig
from views.settingsView import settings
# Funções
from functions.functions import (
    YELLOW, RED, RESET, GREEN, WHITE, RED_BACKGROUND,
    clean, get_keypress, max_digits, acaoInvalida,
)

def main():
    max_digits(999999999)
    while True:
        clean()
        print(GREEN + "OLIMP - TELA INICIAL")
        print(YELLOW + "1) Geometria")
        print("2) Bases")
        print("3) Álgebra")
        print("4) Combinatória")
        print("5) Trigonometria")
        print(RED + "0) Sair" + RESET)
        print("")
        print("Qual ação deseja fazer?:")
        
        escolha = get_keypress()

        if escolha == "1":
            geometria()

        elif escolha == "2":
            base()

        elif escolha == "3":
            algebra()

        elif escolha == "4":
            combinatoria()

        elif escolha == "5":
            trig()

        elif escolha == "s" or escolha == "S":
            settings()

        elif escolha == "0": 
            clean()
            print(GREEN + "OLIMP - TELA INICIAL")
            print(YELLOW + "1) Geometria")
            print("2) Bases")
            print("3) Álgebra")
            print("4) Combinatória")
            print("5) Trigonometria")
            print(RED_BACKGROUND + WHITE + "0) Sair" + RESET)
            print("")
            print("Qual ação deseja fazer?:")
        
            print("")
            print(RED + "Tem certeza que deseja Sair? (Y/n)" + RESET)
            saida = get_keypress()
            if saida == "y" or saida == "Y":
                clean()
                break
        else:
            acaoInvalida()

if __name__ == '__main__':
    main()