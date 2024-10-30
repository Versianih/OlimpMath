from functions.functions import(
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,
)
from functions.baseF import(
    DecimalParaBase,
    BaseParaDecimal,
    BaseParaBase,
)


def base():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> BASE")
        print(YELLOW + "1) Base Decimal para Base n")
        print("2) Base n Para Base Decimal")
        print("3) Base n Para Base m")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Transformar Base Decimal em Base n
        if escolha == "1":
            clean()
            DecimalParaBase(input("Número na Base Decimal:"), input("Base Final:"), True)
            voltar()
        
        # Transformar Base n para Base Decimal
        elif escolha == "2":
            clean()
            BaseParaDecimal(input("Número:"), input("Base:"), True)
            voltar()
        
        # Transformar Base n para Base m
        elif escolha == "3":
            clean()
            BaseParaBase(input("Número Inicial:"), input("Base Inicial:"), input("Base Final:"), True)
            voltar()
        
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()