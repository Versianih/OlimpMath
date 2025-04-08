from InquirerPy import prompt
from functions.tools import(
    Tools,
    GREEN, RED, CYAN, GRENN_BACKGROUND, RESET, WHITE
)

import functions.tools

def settings():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "CONFIGURAÇÕES",
                "choices": [
                            f"Saída de Casas Decimais: {str(functions.tools.casas_decimais)} casas decimais", 
                            f"Saída - Unidade de Medida de Ângulos: {str(functions.tools.saida_angulo)}", 
                            f"Entrada - Unidade de Medida de Ângulos: {str(functions.tools.entrada_angulo)}",
                            "Voltar"
                            ],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == f"Saída de Casas Decimais: {str(functions.tools.casas_decimais)} casas decimais":
            Tools.clean()
            preTratDecimais = input(CYAN + "Casas decimais atual: " + GREEN +  str(functions.tools.casas_decimais) + CYAN +  " Saída Nova:" + RESET)
            if Tools.trat_erro(int, [preTratDecimais]) == True:
                functions.tools.casas_decimais = int(preTratDecimais)
            else:
                Tools.voltar()

        elif escolha == f"Saída - Unidade de Medida de Ângulos: {str(functions.tools.saida_angulo)}":
            saida_angulo()

        elif escolha == f"Entrada - Unidade de Medida de Ângulos: {str(functions.tools.entrada_angulo)}":
            entrada_angulo()
            
        elif escolha == "Voltar":
            Tools.clean()
            break


def saida_angulo():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": f"CONFIGURAÇÕES -> SAÍDA - ÂNGULO = {str(functions.tools.saida_angulo)}",
                "choices": ["Graus", "Radianos", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha != "Voltar":
            functions.tools.saida_angulo = "graus" if escolha == "Graus" else "rad" if escolha == "Radianos" else None
            break

        elif escolha == "Voltar":
            Tools.clean()
            break


def entrada_angulo():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": f"CONFIGURAÇÕES -> ENTRADA - ÂNGULO = {str(functions.tools.entrada_angulo)}",
                "choices": ["Graus", "Radianos", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha != "Voltar":
            functions.tools.entrada_angulo = "graus" if escolha == "Graus" else "rad" if escolha == "Radianos" else None
            break

        else:
            Tools.clean()
            break