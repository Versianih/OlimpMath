import time, os
from funcoes import(
inserirINT, voltar,
DecimalParaBase,
BaseParaDecimal,
BaseParaBase,
)

from funcoes import(
RESET,
RED,
GREEN,
YELLOW,
)

def base():
    while True:
        os.system("cls")
        print(YELLOW + "1) Base Decimal para Base n")
        print("2) Base n Para Base Decimal")
        print("3) Base n Para Base m")
        print(RED + "0) Voltar" + RESET)
        escolha = input("Qual ação deseja fazer?:")

        if escolha == "1":
            os.system("cls")
            DecPBase = DecimalParaBase(inserirINT("Número na Base Decimal:"), inserirINT("Base Final:"))
            print(GREEN + "Número na Base Final:",DecPBase + RESET)
            print("")
            input(voltar())
        
        elif escolha == "2":
            os.system("cls")
            BasePDec = BaseParaDecimal(inserirINT("Número:"), inserirINT("Base:"))
            print(GREEN + "Número na Base Decimal:",BasePDec + RESET)
            print("")
            input(voltar())
        
        elif escolha == "3":
            os.system("cls")
            BasePBase = BaseParaBase(inserirINT("Número Inicial:"), inserirINT("Base Inicial:"), inserirINT("Base Final:"))
            print(GREEN + "Número na Base Final:",BasePBase + RESET)
            print("")
            input(voltar())
        
        elif escolha == "0":
            os.system("cls")
            break
        else:
            print(RED + "Favor selecionar uma ação válida." + RESET)
            time.sleep(1)