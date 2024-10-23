import os
from funcoes import(
    clean, get_keypress, inserirINT, voltar, acaoInvalida, resultado,
    DecimalParaBase,
    BaseParaDecimal,
    BaseParaBase,
)

from funcoes import(
    RESET,
    RED,
    YELLOW,
    GREEN,
)

def base():
    while True:
        clean()
        print(GREEN + "BASE")
        print(YELLOW + "1) Base Decimal para Base n")
        print("2) Base n Para Base Decimal")
        print("3) Base n Para Base m")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        if escolha == "1":
            clean()
            DecPBase = DecimalParaBase(inserirINT("Número na Base Decimal:"), inserirINT("Base Final:"))
            resultado(DecPBase)
            voltar()
        
        elif escolha == "2":
            clean()
            BasePDec = BaseParaDecimal(inserirINT("Número:"), inserirINT("Base:"))
            resultado(BasePDec)
            voltar()
        
        elif escolha == "3":
            clean()
            BasePBase = BaseParaBase(inserirINT("Número Inicial:"), inserirINT("Base Inicial:"), inserirINT("Base Final:"))
            resultado(BasePBase)
            voltar()
        
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()