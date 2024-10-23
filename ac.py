from funcoes import(
    clean, get_keypress, inserirINT,voltar, acaoInvalida, resultado,
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

        if escolha == "1":
            clean()
            CombinacaoNP = Combinação(inserirINT("Insira N:"), inserirINT("Insira P:"))
            resultado(CombinacaoNP)
            voltar()
        
        elif escolha == "2":
            clean()
            PermutacaoNK = PermutaçãoDeNemK(inserirINT("Insira N:"), inserirINT("Insira K:"))
            resultado(PermutacaoNK)
            voltar()
        
        elif escolha == "3":
            clean()
            PermutacaoCirc = PermutaçãoCircular(inserirINT("Número de Elementos: "))
            resultado(PermutacaoCirc)
            voltar()
        
        elif escolha == "4":
            clean()
            fact = Fatorial(inserirINT("Número:"))
            resultado(fact)
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()