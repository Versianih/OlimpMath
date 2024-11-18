from functions.functions import(
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,
)
from functions.combinatoriaF import(
    Combinação,
    CombinaçãoCompleta,
    PermutaçãoDeNemK,
    PermutaçãoCircular,
    PermutaçãoCaótica,
    Fatorial,
)


def combinatoria():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> COMBINATÓRIA")
        print(YELLOW + "1) Combinação de N escolhe P")
        print("2) Combinação Completa de N e P")
        print("3) Permutação de N em K")
        print("4) Permutação Circular")
        print("5) Permutação Caótica")
        print("6) Fatorial de um Número")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")        
        escolha = get_keypress()

        # Combinação
        if escolha == "1":
            clean()
            Combinação(input("Insira N:"), input("Insira P:"), imprimir=True)
            voltar()
        
        # Combinação Completa
        elif escolha == "2":
            clean()
            CombinaçãoCompleta(input("Insira N:"), input("Insira P:"), imprimir=True)
            voltar()

        # Permutação
        elif escolha == "3":
            clean()
            PermutaçãoDeNemK(input("Insira N:"), input("Insira K:"), imprimir=True)
            voltar()
        
        # Permutação Circular
        elif escolha == "4":
            clean()
            PermutaçãoCircular(input("Número de Elementos: "), imprimir=True)
            voltar()
        
        # Permutação Caótica
        elif escolha == "5":
            clean()
            PermutaçãoCaótica(input("Quantidade de Elementos:"), imprimir=True)
            voltar()
            
        # Fatorial
        elif escolha == "6":
            clean()
            Fatorial(input("Número:"), imprimir=True)
            voltar()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()