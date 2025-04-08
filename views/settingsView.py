import os
from InquirerPy import prompt
from functions.tools import(
    Tools,
    GREEN, RED, CYAN, GRENN_BACKGROUND, RESET, WHITE,
)
from dotenv import load_dotenv, set_key

def settings(CASAS_DECIMAIS, SAIDA_ANGULO, ENTRADA_ANGULO):
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "CONFIGURAÇÕES",
                "choices": [
                            f"Saída de Casas Decimais: {str(CASAS_DECIMAIS)} casas decimais", 
                            f"Saída - Unidade de Medida de Ângulos: {str(SAIDA_ANGULO)}", 
                            f"Entrada - Unidade de Medida de Ângulos: {str(ENTRADA_ANGULO)}",
                            "",
                            "Salvar Configurações(Essa ação salva as configurações e sai do programa)"
                            ],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == f"Saída de Casas Decimais: {str(CASAS_DECIMAIS)} casas decimais":
            Tools.clean()
            preTratDecimais = input(CYAN + "Casas decimais atual: " + GREEN +  str(CASAS_DECIMAIS) + CYAN +  " Saída Nova:" + RESET)
            if Tools.trat_erro(int, [preTratDecimais]):
                CASAS_DECIMAIS = int(preTratDecimais)
                set_key('.env', 'CASAS_DECIMAIS', preTratDecimais)
            else:
                Tools.voltar()


        elif escolha == f"Saída - Unidade de Medida de Ângulos: {str(SAIDA_ANGULO)}":
            Tools.clean()
            campos = [
                {
                    "type": "list",
                    "message": f"CONFIGURAÇÕES -> SAÍDA - ÂNGULO = {str(SAIDA_ANGULO)}",
                    "choices": ["Graus", "Radianos", "Voltar"],
                }
            ]
            escolha = prompt(campos)
            escolha = escolha.get(0)

            if escolha != "Voltar":
                SAIDA_ANGULO = "graus" if escolha == "Graus" else "rad" if escolha == "Radianos" else None
                set_key('.env', 'SAIDA_ANGULO', SAIDA_ANGULO)
                pass

            elif escolha == "Voltar":
                Tools.clean()
                pass


        elif escolha == f"Entrada - Unidade de Medida de Ângulos: {str(ENTRADA_ANGULO)}":
            Tools.clean()
            campos = [
                {
                    "type": "list",
                    "message": f"CONFIGURAÇÕES -> ENTRADA - ÂNGULO = {str(ENTRADA_ANGULO)}",
                    "choices": ["Graus", "Radianos", "Voltar"],
                }
            ]
            escolha = prompt(campos)
            escolha = escolha.get(0)

            if escolha != "Voltar":
                ENTRADA_ANGULO = "graus" if escolha == "Graus" else "rad" if escolha == "Radianos" else None
                set_key('.env', 'ENTRADA_ANGULO', ENTRADA_ANGULO)
                pass

            else:
                Tools.clean()
                pass


        elif escolha == "Salvar Configurações(Essa ação salva as configurações e sai do programa)":
            Tools.clean()
            # Gambiarra porca para o programa ler novamente o arquivo .env
            exit()