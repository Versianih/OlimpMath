# Telas
from views.geo import geometria
from views.base import base
from views.algebra import algebra
from views.ac import ac
from views.trig import trig
# Funções
from funcoes import (
    YELLOW, RED, RESET, GREEN,
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
        print("5) Trigonometria Plana")
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
            ac()

        elif escolha == "5":
            trig()

        elif escolha == "0": 
            clean()
            break
        else:
            acaoInvalida()

if __name__ == '__main__':
    main()