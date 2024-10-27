from funcoes import(
    clean, get_keypress, voltar, acaoInvalida,
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
            DecimalParaBase(input("Número na Base Decimal:"), input("Base Final:"))
            voltar()
        
        elif escolha == "2":
            clean()
            BaseParaDecimal(input("Número:"), input("Base:"))
            voltar()
        
        elif escolha == "3":
            clean()
            BaseParaBase(input("Número Inicial:"), input("Base Inicial:"), input("Base Final:"))
            voltar()
        
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()