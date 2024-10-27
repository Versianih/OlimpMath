from funcoes import(
    clean, get_keypress, voltar, acaoInvalida,
    
    Combinação,
    PermutaçãoDeNemK,
    PermutaçãoCircular,
    Fatorial,
)

from funcoes import(
    RESET,
    RED,
    YELLOW,
    GREEN,
)

def ac():
    while True:
        clean()
        print(GREEN + "COMBINATÓRIA")
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
            Combinação(input("Insira N:"), input("Insira P:"))
            voltar()
        
        # Permutação
        elif escolha == "2":
            clean()
            PermutaçãoDeNemK(input("Insira N:"), input("Insira K:"))
            voltar()
        
        # Permutação Circular
        elif escolha == "3":
            clean()
            PermutaçãoCircular(input("Número de Elementos: "))
            voltar()
        
        # Fatorial
        elif escolha == "4":
            clean()
            Fatorial(input("Número:"))
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()