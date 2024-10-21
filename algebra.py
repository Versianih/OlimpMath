import os  
from funcoes import(
    inserirFLOAT, inserirINT, voltar, acaoInvalida, resultado,
    raizQuadrada,
    MDC,
    MMC,
    Resto,
    equação2Grau,
)

from funcoes import(
    RESET,
    RED,
    YELLOW,
)

def algebra():
    while True:
        os.system("cls")
        print(YELLOW + "1) Raiz Quadrada")
        print("2) MDC de Dois Números")
        print("3) MMC de Dois Números")
        print("4) Resto de uma Divisão de dois Números")
        print("5) Equações de 2º Grau")
        print(RED + "0) Voltar" + RESET)
        print("")
        escolha = input("Qual ação deseja fazer?:")
        
        if escolha == "1":
            os.system("cls")
            raiz = raizQuadrada(inserirFLOAT("Número que se deseja calcular a Raiz Quadrada:"))
            resultado(raiz)
            voltar()

        elif escolha == "2":
            os.system("cls")
            mdc = MDC(inserirINT("N₁:"), inserirINT("N₂:"))
            resultado(mdc)
            voltar()

        elif escolha == "3":
            os.system("cls")
            mmc = MMC(inserirINT("N₁:"), inserirINT("N₂:"))
            resultado(mmc)
            voltar()

        elif escolha == "4":
            os.system("cls")
            rest = Resto(inserirFLOAT("Dividendo:"), inserirFLOAT("Divisor:"))
            resultado(rest)
            voltar()

        elif escolha == "5":
            os.system("cls")
            solucao2grau = equação2Grau(inserirFLOAT("a:"), inserirFLOAT("b:"), inserirFLOAT("c:"))
            resultado(solucao2grau)
            voltar()

        elif escolha == "0":
            os.system("cls")
            break
        else:
            acaoInvalida()