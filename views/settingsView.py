from InquirerPy import prompt
from functions.functions import(
    acao_invalida, voltar,  clean, trat_erro,
    GREEN, RED, CYAN, GRENN_BACKGROUND, RESET, WHITE
)

import functions.functions

def settings():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "CONFIGURAÇÕES",
                "choices": [
                            f"Saída de Casas Decimais: {str(functions.functions.casas_decimais)} casas decimais", 
                            f"Saída - Unidade de Medida de Ângulos: {str(functions.functions.saida_angulo)}", 
                            f"Entrada - Unidade de Medida de Ângulos: {str(functions.functions.entrada_angulo)}",
                            "Voltar"
                            ],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == f"Saída de Casas Decimais: {str(functions.functions.casas_decimais)} casas decimais":
            clean()
            preTratDecimais = input(CYAN + "Casas decimais atual: " + GREEN +  str(functions.functions.casas_decimais) + CYAN +  " Saída Nova:" + RESET)
            if trat_erro(int, [preTratDecimais]) == True:
                functions.functions.casas_decimais = int(preTratDecimais)
            else:
                voltar()

        elif escolha == f"Saída - Unidade de Medida de Ângulos: {str(functions.functions.saida_angulo)}":
            saidaÂngulo()

        elif escolha == f"Entrada - Unidade de Medida de Ângulos: {str(functions.functions.entrada_angulo)}":
            entradaAngulo()
            
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def saidaÂngulo():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": f"CONFIGURAÇÕES -> SAÍDA - ÂNGULO = {str(functions.functions.saida_angulo)}",
                "choices": ["Graus", "Radianos", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == "Graus":
            functions.functions.saida_angulo = "graus"
            break
        
        elif escolha == "Radianos":
            functions.functions.saida_angulo = "rad"
            break

        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def entradaAngulo():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": f"CONFIGURAÇÕES -> ENTRADA - ÂNGULO = {str(functions.functions.entrada_angulo)}",
                "choices": ["Graus", "Radianos", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == "Graus":
            functions.functions.entrada_angulo = "graus"
            break

        elif escolha == "Radianos":
            functions.functions.entrada_angulo = "rad"
            break

        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()