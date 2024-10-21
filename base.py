import os
from funcoes import(
    inserirINT, voltar, acaoInvalida, resultado,
    DecimalParaBase,
    BaseParaDecimal,
    BaseParaBase,
)

from funcoes import(
    RESET,
    RED,
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
            resultado(DecPBase)
            voltar()
        
        elif escolha == "2":
            os.system("cls")
            BasePDec = BaseParaDecimal(inserirINT("Número:"), inserirINT("Base:"))
            resultado(BasePDec)
            voltar()
        
        elif escolha == "3":
            os.system("cls")
            BasePBase = BaseParaBase(inserirINT("Número Inicial:"), inserirINT("Base Inicial:"), inserirINT("Base Final:"))
            resultado(BasePBase)
            voltar()
        
        elif escolha == "0":
            os.system("cls")
            break
        else:
            acaoInvalida()