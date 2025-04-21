from InquirerPy import prompt
from functions.tools import Tools
from functions.base import Base


def base():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "BASE",
                "choices": ["10 -> n", "n -> 10", "n -> m", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Transformar Base Decimal em Base n
        if escolha == "10 -> n":
            Tools.clean()
            Base.decimal_para_base(input("Número na Base Decimal:"), input("Base Final:"), True)
            Tools.voltar()
        
        # Transformar Base n para Base Decimal
        elif escolha == "n -> 10":
            Tools.clean()
            Base.base_para_decimal(input("Número:"), input("Base:"), True)
            Tools.voltar()
        
        # Transformar Base n para Base m
        elif escolha == "n -> m":
            Tools.clean()
            Base.base_para_base(input("Número Inicial:"), input("Base Inicial:"), input("Base Final:"), True)
            Tools.voltar()
        
        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break