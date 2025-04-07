from functions.functions import (
    clean, acao_invalida, 
)
from views.geoView.geoPlanaView import geometria_plana
from views.geoView.geoEspacialView import geometria_espacial
from views.geoView.geoAnaliticaView import geometria_analitica
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
            geometria_plana()

        # Geometria Espacial
        elif escolha == "Geometria Espacial":
            geometria_espacial()

        # Geometria Analítica
        elif escolha == "Geometria Analítica":
            geometria_analitica()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()