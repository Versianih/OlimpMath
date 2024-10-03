import time, os  
from funcoes import(
inserirINT,voltar,
Combinação,
PermutaçãoDeNemK,
PermutaçãoCircular,
)

from funcoes import(
RESET,
RED,
GREEN,
YELLOW,
)


while True:
    os.system("cls")
    print(YELLOW + "1) Combinação de N em K")
    print("2) Permutação de N em K")
    print("3) Permutação Circular")
    print(RED + "0) Sair" + RESET)
    escolha = input("Qual ação deseja fazer?:")

    if escolha == "1":
        os.system("cls")
        CombinacaoNK = (inserirINT("Insira N:"), inserirINT("Insira K:"))
        print(GREEN + "Resultado:", CombinacaoNK + RESET)
        print("")
        input(voltar())
    
    elif escolha == "2":
        os.system("cls")
        PermutacaoNK = PermutaçãoDeNemK(inserirINT("Insira N:"), inserirINT("Insira K:"))
        print(GREEN + "Resultado:",PermutacaoNK + RESET)
        print("")
        input(voltar())
    
    elif escolha == "3":
        os.system("cls")
        PermutacaoCirc = PermutaçãoCircular(inserirINT("Número de Elementos"))
        print(GREEN + "Resultado:",PermutacaoCirc + RESET)
        print("")
        input(voltar())
    
    elif escolha == "0":
        os.system("cls")
        break
    else:
        print(RED + "Favor selecionar uma ação válida." + RESET)
        time.sleep(1)