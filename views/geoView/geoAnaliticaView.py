from InquirerPy import prompt
from functions.tools import Tools

from functions.geoFunctions.geoAnalitica import (
    distancia_entre_pontos,
    retangulos_em_uma_malha,
)


def geometria_analitica():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA ANALÍTICA",
                "choices": ["Distância Entre Dois Pontos", "Retângulos em uma malha", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Dist. entre pontos
        if escolha == "Distância Entre Dois Pontos":
            Tools.clean()
            distancia_entre_pontos(input("Xa:"), input("Ya:"), input("Xb:"), input("Yb:"), True)
            Tools.voltar()

        elif escolha == "Retângulos em uma malha":
            Tools.clean()
            retangulos_em_uma_malha(input("Base da malha:"), input("Altura da malha:"), True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break