from functions.functions import(
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,
)
from functions.algebraF import(
    raizQuadrada,
    MDC,
    MMC,
    Resto,
    equação2Grau,
)


def algebra():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> ÁLGEBRA")
        print(YELLOW + "1) Raiz Quadrada")
        print("2) MDC de Dois Números")
        print("3) MMC de Dois Números")
        print("4) Resto de uma Divisão de dois Números")
        print("5) Equações de 2º Grau")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()
        
        # Raiz Quadrada
        if escolha == "1":
            clean()
            raizQuadrada(input("Número que se deseja calcular a Raiz Quadrada:"))
            voltar()

        # MDC
        elif escolha == "2":
            clean()
            MDC(input("N₁:"), input("N₂:"))
            voltar()

        # MMC
        elif escolha == "3":
            clean()
            MMC(input("N₁:"), input("N₂:"))
            voltar()

        # Resto
        elif escolha == "4":
            clean()
            Resto(input("Dividendo:"), input("Divisor:"))
            voltar()

        # Equação de Grau 2
        elif escolha == "5":
            clean()
            equação2Grau(input("a:"), input("b:"), input("c:"))
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()