from InquirerPy import prompt
from functions.functions import(
    clean, voltar, acao_invalida,
)
from functions.baseF import(
    decimal_para_base,
    base_para_decimal,
    base_para_base,
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
            decimal_para_base(input("Número na Base Decimal:"), input("Base Final:"), True)
            voltar()
        
        # Transformar Base n para Base Decimal
        elif escolha == "n -> 10":
            clean()
            base_para_decimal(input("Número:"), input("Base:"), True)
            voltar()
        
        # Transformar Base n para Base m
        elif escolha == "n -> m":
            clean()
            base_para_base(input("Número Inicial:"), input("Base Inicial:"), input("Base Final:"), True)
            voltar()
        
        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()