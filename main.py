import os, time
from area import area
from base import base 
from algebra import algebra
from ac import ac
from trig import trig
from funcoes import(
    YELLOW, RED, GREEN, RESET,
    acaoInvalida,
)




while True:
    os.system("cls")
    print(YELLOW + "1) Área")
    print("2) Bases")
    print("3) Álgebra")
    print("4) Combinatória")
    print("5) Trigonometria Plana")
    print(RED + "0) Sair" + RESET)
    print("")
    escolha = input("Qual ação deseja fazer?:")

    if escolha == "1":
        area()

    elif escolha == "2":
        base()

    elif escolha == "3":
        algebra()

    elif escolha == "4":
        ac()

    elif escolha == "5":
        trig()

    elif escolha == "0":
        os.system("cls")
        break

    else:
        acaoInvalida()