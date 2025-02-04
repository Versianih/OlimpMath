from InquirerPy import prompt
from functions.functions import (
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from functions.geoFunctions.geoAnalitica import (
    distPontos,
)


def geometriaAnalítica():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA ANALÍTICA",
                "choices": ["Distância Entre Dois Pontos", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Dist. entre pontos
        if escolha == "Distância Entre Dois Pontos":
            clean()
            distPontos(input("Xa:"), input("Ya:"), input("Xb:"), input("Yb:"), True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()