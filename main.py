# Telas
from views.geoView.geoView import geometria
from views.baseView import base
from views.algebraView import algebra
from views.combinatoriaView import combinatoria
from views.trigView import trig
from views.settingsView import settings
# Funções
from functions.tools import Tools
from InquirerPy import prompt


def main():
    Tools.max_digits(999999999)
    while True:
        Tools.clean()

        campos = [
            {
                "type": "list",
                "message": "OLIMP - TELA INICIAL",
                "choices": ["Geometria", "Bases", "Álgebra", "Combinatória", "Trigonometria", "Configurações", "Sair"],
            }
        ]

        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == "Geometria":
            geometria()

        elif escolha == "Bases":
            base()

        elif escolha == "Álgebra":
            algebra()

        elif escolha == "Combinatória":
            combinatoria()

        elif escolha == "Trigonometria":
            trig()

        elif escolha == "Configurações":
            settings()

        elif escolha == "Sair": 
            Tools.clean()
            campos_sair = [
                {
                    "type": "list",
                    "message": "Tem certeza que deseja sair?",
                    "choices": ["Sim", "Não"],
                }
            ]

            saida = prompt(campos_sair)
            saida = saida.get(0)

            if saida == "Sim":
                Tools.clean()
                break

if __name__ == '__main__':
    main()