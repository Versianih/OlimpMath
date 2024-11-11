from functions.functions import(
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,
)

# Básico
from functions.algebraF import(
    Radiciação,
    Exponenciação,
    MDC,
    MMC,
    Resto,
)

# Polinômios
from functions.algebraF import(
    equação2Grau,
)

# Progressões
from functions.algebraF import(
    Somatório,
    Produtório
)


def algebra():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> ÁLGEBRA")
        print(YELLOW + "1) Básico +")
        print("2) Polinômios +")
        print("3) Progressões +")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()
        
        # Básico
        if escolha == "1":
            clean()
            algebraBásico()

        # Polinômios
        elif escolha == "2":
            clean()
            algebraPolinomios()

        # Progressões
        elif escolha == "3":
            clean()
            algebraProgressões()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def algebraBásico():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> ÁLGEBRA -> BÁSICO")
        print(YELLOW + "1) Radiciação")
        print("2) Exponenciação")
        print("3) MDC de Dois Números")
        print("4) MMC de Dois Números")
        print("5) Resto de uma Divisão de dois Números")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Radiciação
        if escolha == "1":
            clean()
            Radiciação(input("Número/Expressão dentro da Raiz:"), input("Índice da Raiz:"), True)
            voltar()

        # Exponenciação
        if escolha == "2":
            clean()
            Exponenciação(input("Base:"), input("Expoente:"), True)
            voltar()

        # MDC
        elif escolha == "3":
            clean()
            MDC(input("N₁:"), input("N₂:"), True)
            voltar()

        # MMC
        elif escolha == "4":
            clean()
            MMC(input("N₁:"), input("N₂:"), True)
            voltar()

        # Resto
        elif escolha == "5":
            clean()
            Resto(input("Dividendo:"), input("Divisor:"), True)
            voltar()

        # Sair
        if escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def algebraPolinomios():
    while True: 
        clean()
        print(GREEN + "TELA INICIAL -> ÁLGEBRA -> POLINÔMIOS")
        print(YELLOW + "1) Equações de 2º Grau")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Equação de Segundo Grau
        if escolha == "1":
            clean()
            equação2Grau(input("a:"), input("b:"), input("c:"), True)
            voltar()

        # Sair
        if escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def algebraProgressões():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> ÁLGEBRA -> PROGRESSÕES")
        print(YELLOW + "1) Somatório")
        print("2) Produtório")
        print("3) PA +")
        print("4) PG +")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Somatório
        if escolha == "1":
            clean()
            Somatório(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        # Produtório
        elif escolha == "2":
            clean()
            Produtório(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()