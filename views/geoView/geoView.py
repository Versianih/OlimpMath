from functions.functions import (
    clean, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from views.geoView.geoPlanaView import geometriaPlana
from views.geoView.geoEspacialView import geometriaEspacial
from views.geoView.geoAnaliticaView import geometriaAnalítica
from InquirerPy import prompt


def geometria():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA",
                "choices": ["Geometria Plana", "Geometria Espacial", "Geometria Analítica", "Voltar"],
            }
        ]

        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Geometria Plana
        if escolha == "Geometria Plana":
            geometriaPlana()

        # Geometria Espacial
        elif escolha == "Geometria Espacial":
            geometriaEspacial()

        # Geometria Analítica
        elif escolha == "Geometria Analítica":
            geometriaAnalítica()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()