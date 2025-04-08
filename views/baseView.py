from InquirerPy import prompt
from functions.tools import Tools
from functions.baseF import(
    decimal_para_base,
    base_para_decimal,
    base_para_base,
)


def base():
    while True:
        Tools.clean()
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
            Tools.clean()
            decimal_para_base(input("Número na Base Decimal:"), input("Base Final:"), True)
            Tools.voltar()
        
        # Transformar Base n para Base Decimal
        elif escolha == "n -> 10":
            Tools.clean()
            base_para_decimal(input("Número:"), input("Base:"), True)
            Tools.voltar()
        
        # Transformar Base n para Base m
        elif escolha == "n -> m":
            Tools.clean()
            base_para_base(input("Número Inicial:"), input("Base Inicial:"), input("Base Final:"), True)
            Tools.voltar()
        
        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break