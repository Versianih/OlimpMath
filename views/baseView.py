from InquirerPy import prompt
from functions.functions import(
    clean, voltar, acaoInvalida,
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
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> BASE",
                "choices": ["10 -> n", "n -> 10", "n -> m", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Transformar Base Decimal em Base n
        if escolha == "10 -> n":
            clean()
            DecimalParaBase(input("Número na Base Decimal:"), input("Base Final:"), True)
            voltar()
        
        # Transformar Base n para Base Decimal
        elif escolha == "n -> 10":
            clean()
            BaseParaDecimal(input("Número:"), input("Base:"), True)
            voltar()
        
        # Transformar Base n para Base m
        elif escolha == "n -> m":
            clean()
            BaseParaBase(input("Número Inicial:"), input("Base Inicial:"), input("Base Final:"), True)
            voltar()
        
        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()