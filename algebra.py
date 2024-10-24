from funcoes import(
    clean, get_keypress, voltar, acaoInvalida,
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
    GREEN,
)

def algebra():
    while True:
        clean()
        print(GREEN + "ÁLGEBRA")
        print(YELLOW + "1) Raiz Quadrada")
        print("2) MDC de Dois Números")
        print("3) MMC de Dois Números")
        print("4) Resto de uma Divisão de dois Números")
        print("5) Equações de 2º Grau")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()
        
        if escolha == "1":
            clean()
            raizQuadrada(input("Número que se deseja calcular a Raiz Quadrada:"))
            voltar()

        elif escolha == "2":
            clean()
            MDC(input("N₁:"), input("N₂:"))
            voltar()

        elif escolha == "3":
            clean()
            MMC(input("N₁:"), input("N₂:"))
            voltar()

        elif escolha == "4":
            clean()
            Resto(input("Dividendo:"), input("Divisor:"))
            voltar()

        elif escolha == "5":
            clean()
            equação2Grau(input("a:"), input("b:"), input("c:"))
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()