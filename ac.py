import os  
from funcoes import(
    inserirINT,voltar, acaoInvalida, resultado,
    Combinação,
    PermutaçãoDeNemK,
    PermutaçãoCircular,
    Fatorial,
)

from funcoes import(
    RESET,
    RED,
    YELLOW,
)

def ac():
    while True:
        os.system("cls")
        print(YELLOW + "1) Combinação de N escolhe P")
        print("2) Permutação de N em K")
        print("3) Permutação Circular")
        print("4) Fatorial de um Número")
        print(RED + "0) Voltar" + RESET)
        escolha = input("Qual ação deseja fazer?:")

        if escolha == "1":
            os.system("cls")
            CombinacaoNP = Combinação(inserirINT("Insira N:"), inserirINT("Insira P:"))
            resultado(CombinacaoNP)
            voltar()
        
        elif escolha == "2":
            os.system("cls")
            PermutacaoNK = PermutaçãoDeNemK(inserirINT("Insira N:"), inserirINT("Insira K:"))
            resultado(PermutacaoNK)
            voltar()
        
        elif escolha == "3":
            os.system("cls")
            PermutacaoCirc = PermutaçãoCircular(inserirINT("Número de Elementos: "))
            resultado(PermutacaoCirc)
            voltar()
        
        elif escolha == "4":
            os.system("cls")
            fact = Fatorial(inserirINT("Número:"))
            resultado(fact)
            voltar()

        elif escolha == "0":
            os.system("cls")
            break
        else:
            acaoInvalida()