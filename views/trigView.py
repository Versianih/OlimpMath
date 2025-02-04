from InquirerPy import prompt
from functions.functions import(
    voltar, acaoInvalida, get_keypress, clean,
    RESET, RED, YELLOW, GREEN,
)
from functions.trigF import(
    # Hipotenusa
    HipotenusaComOposto,
    HipotenusaComAdjacente,
    # Oposto
    OpostoComHipotenusa,
    OpostoComAdjacente,
    # Adjacente
    AdjacenteComHipotenusa,
    AdjacenteComOposto,
    # Ângulo
    AnguloComCOCA,
    AnguloComCOH,
    AnguloComCAH,
)
import functions.functions


def trig():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> TRIGONOMETRIA",
                "choices": ["Calcular Hipotenusa", "Calcular Cateto Oposto", "Calcular Cateto Adjacente", "Calcular Ângulo", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == "Calcular Hipotenusa":
            hipotenusa()

        elif escolha == "Calcular Cateto Oposto":
            oposto()
        
        elif escolha == "Calcular Cateto Adjacente":
            adjacente()

        elif escolha == "Calcular Ângulo":
            angulo()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def hipotenusa():
    while True:
        clean()
        campos_hipotenusa = [
            {
                "type": "list",
                "message": "TELA INICIAL -> TRIGONOMETRIA -> HIPOTENUSA",
                "choices": ["Cateto Oposto", "Cateto Adjacente", "Voltar"],
            }
        ]
        escolha_hipotenusa = prompt(campos_hipotenusa)
        escolha_hipotenusa = escolha_hipotenusa.get(0)

        if escolha_hipotenusa == "Cateto Oposto":
            clean()
            HipotenusaComOposto(input("Cateto Oposto:"), input("Ângulo em " + str(functions.functions.entrada_angulo) + ":"), True)
            voltar()

        elif escolha_hipotenusa == "Cateto Adjacente":
            clean()
            HipotenusaComAdjacente(input("Cateto Adjacente:"), input("Ângulo em " + str(functions.functions.entrada_angulo) + ":"), True)
            voltar()
            
        elif escolha_hipotenusa == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def oposto():
    while True:
        clean()
        campos_oposto = [
            {
                "type": "list",
                "message": "TELA INICIAL -> TRIGONOMETRIA -> CATETO OPOSTO",
                "choices": ["Hipotenusa", "Cateto Adjacente", "Voltar"],
            }
        ]
        escolha_oposto = prompt(campos_oposto)
        escolha_oposto = escolha_oposto.get(0)

        
        if escolha_oposto == "Hipotenusa":
            clean()
            OpostoComHipotenusa(input("Hipotenusa:"), input("Ângulo em " + str(functions.functions.entrada_angulo) + ":"), True)
            voltar()

        elif escolha_oposto == "Cateto Adjacente":
            clean()
            OpostoComAdjacente(input("Cateto Adjacente:"), input("Ângulo em " + str(functions.functions.entrada_angulo) + ":"), True)
            voltar()
        
        elif escolha_oposto == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def adjacente():
    while True:
        clean()
        campos_adjacente = [
            {
                "type": "list",
                "message": "TELA INICIAL -> TRIGONOMETRIA -> ADJACENTE",
                "choices": ["Hipotenusa", "Cateto Oposto", "Voltar"],
            }
        ]
        escolha_adjacente = prompt(campos_adjacente)
        escolha_adjacente = escolha_adjacente.get(0)

        
        if escolha_adjacente == "Hipotenusa":
            clean()
            AdjacenteComHipotenusa(input("Hipotenusa:"), input("Ângulo em " + str(functions.functions.entrada_angulo) + ":"), True)
            voltar()

        elif escolha_adjacente == "Cateto Oposto":
            clean()
            AdjacenteComOposto(input("Cateto Adjacente:"), input("Ângulo em " + str(functions.functions.entrada_angulo) + ":"), True)
            voltar()

        # Voltar
        elif escolha_adjacente == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def angulo():
    while True:
        clean()
        campos_angulo = [
            {
                "type": "list",
                "message": "TELA INICIAL -> TRIGONOMETRIA -> ÂNGULO",
                "choices": ["CO/CA", "CO/H", "CA/H", "Voltar"],
            }
        ]
        escolha_angulo = prompt(campos_angulo)
        escolha_angulo = escolha_angulo.get(0)

        if escolha_angulo == "CO/CA":
            clean()
            AnguloComCOCA(input("Cateto Oposto:"), input("Cateto Adjacente:"), True)
            voltar()

        elif escolha_angulo == "CO/H":
            clean()
            AnguloComCOH(input("Cateto Oposto:"), input("Hipotenusa:"), True)
            voltar()

        elif escolha_angulo == "CA/H":
            clean()
            AnguloComCAH(input("Cateto Adjacente:"), input("Hipotenusa"), True)
            voltar()
        
        # Voltar
        elif escolha_angulo == "Voltar":
            clean()
            break
        else:
            acaoInvalida()