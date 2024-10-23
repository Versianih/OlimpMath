from funcoes import(
    clean, get_keypress, inserirFLOAT, inserirINT, voltar, acaoInvalida, resultado,
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
            raiz = raizQuadrada(inserirFLOAT("Número que se deseja calcular a Raiz Quadrada:"))
            resultado(raiz)
            voltar()

        elif escolha == "2":
            clean()
            mdc = MDC(inserirINT("N₁:"), inserirINT("N₂:"))
            resultado(mdc)
            voltar()

        elif escolha == "3":
            clean()
            mmc = MMC(inserirINT("N₁:"), inserirINT("N₂:"))
            resultado(mmc)
            voltar()

        elif escolha == "4":
            clean()
            rest = Resto(inserirFLOAT("Dividendo:"), inserirFLOAT("Divisor:"))
            resultado(rest)
            voltar()

        elif escolha == "5":
            clean()
            solucao2grau = equação2Grau(inserirFLOAT("a:"), inserirFLOAT("b:"), inserirFLOAT("c:"))
            resultado(solucao2grau)
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()