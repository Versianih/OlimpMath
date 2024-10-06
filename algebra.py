import time, os  
from funcoes import(
inserirFLOAT, inserirINT, voltar, acaoInvalida,
raizQuadrada,
MDC,
Resto,
equação2Grau,
)

from funcoes import(
RESET,
RED,
GREEN,
YELLOW,
)

def algebra():
    pass


while True:
    os.system("cls")
    print(YELLOW + "1) Raiz Quadrada")
    print("2) MDC de Dois Números")
    print("3) Resto de uma Divisão de dois Números")
    print("4) Equações de 2º Grau")
    print(RED + "0) Sair" + RESET)
    print("")
    escolha = input("Qual ação deseja fazer?:")
    
    if escolha == "1":
        os.system("cls")
        raiz = raizQuadrada(inserirFLOAT("Número que se deseja calcular a Raiz Quadrada:"))
        print(GREEN + "Resultado:",raiz,"" + RESET)
        print("")
        input(voltar())

    elif escolha == "2":
        os.system("cls")
        mdc = MDC(inserirFLOAT("N₁:"), inserirFLOAT("N₂:"))
        print(GREEN + "Resultado:",mdc,"" + RESET)
        print("")
        input(voltar())

    elif escolha == "3":
        os.system("cls")
        rest = Resto(inserirFLOAT("Dividendo:"), inserirFLOAT("Divisor:"))
        print(GREEN + "Resto:",rest,"" + RESET)
        print("")
        input(voltar())

    elif escolha == "4":
        os.system("cls")
        solucao2grau = equação2Grau(inserirFLOAT("a:"), inserirFLOAT("b:"), inserirFLOAT("c:"))
        print(GREEN + solucao2grau + RESET)
        print("")
        input(voltar())

    elif escolha == "0":
        os.system("cls")
        break

    else:
        acaoInvalida()