from functions.functions import(
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,
)
from functions.combinatoriaF import(
    Combinação,
    PermutaçãoDeNemK,
    PermutaçãoCircular,
    Fatorial,
)


def combinatoria():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> COMBINATÓRIA")
        print(YELLOW + "1) Combinação de N escolhe P")
        print("2) Permutação de N em K")
        print("3) Permutação Circular")
        print("4) Fatorial de um Número")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")        
        escolha = get_keypress()

        # Combinação
        if escolha == "1":
            clean()
            Combinação(input("Insira N:"), input("Insira P:"), True)
            voltar()
        
        # Permutação
        elif escolha == "2":
            clean()
            PermutaçãoDeNemK(input("Insira N:"), input("Insira K:"), True)
            voltar()
        
        # Permutação Circular
        elif escolha == "3":
            clean()
            PermutaçãoCircular(input("Número de Elementos: "), True)
            voltar()
        
        # Fatorial
        elif escolha == "4":
            clean()
            Fatorial(input("Número:"), True)
            voltar()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()