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
    Somatório,
    Produtório,
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
        print("6) Somatório")
        print("7) Produtório")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()
        
        # Raiz Quadrada
        if escolha == "1":
            clean()
            raizQuadrada(input("Número que se deseja calcular a Raiz Quadrada:"), True)
            voltar()

        # MDC
        elif escolha == "2":
            clean()
            MDC(input("N₁:"), input("N₂:"), True)
            voltar()

        # MMC
        elif escolha == "3":
            clean()
            MMC(input("N₁:"), input("N₂:"), True)
            voltar()

        # Resto
        elif escolha == "4":
            clean()
            Resto(input("Dividendo:"), input("Divisor:"), True)
            voltar()

        # Equação de Grau 2
        elif escolha == "5":
            clean()
            equação2Grau(input("a:"), input("b:"), input("c:"), True)
            voltar()

        elif escolha == "6":
            clean()
            Somatório(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        elif escolha == "7":
            clean()
            Produtório(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()