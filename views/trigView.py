from InquirerPy import prompt
from functions.tools import(
    Tools,
    RESET, RED, YELLOW, GREEN,
)
from functions.trigF import(
    # Hipotenusa
    hipotenusa_com_oposto,
    hipotenusa_com_adjacente,
    # Oposto
    oposto_com_hipotenusa,
    oposto_com_adjacente,
    # Adjacente
    adjacente_com_hipotenusa,
    adjacente_com_oposto,
    # Ângulo
    angulo_com_coca,
    angulo_com_coh,
    angulo_com_cah,
)
import functions.tools


def trig():
    while True:
        Tools.clean()
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
            Tools.clean()
            break


def hipotenusa():
    while True:
        Tools.clean()
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
            Tools.clean()
            hipotenusa_com_oposto(input("Cateto Oposto:"), input("Ângulo em " + str(functions.tools.entrada_angulo) + ":"), True)
            Tools.voltar()

        elif escolha_hipotenusa == "Cateto Adjacente":
            Tools.clean()
            hipotenusa_com_adjacente(input("Cateto Adjacente:"), input("Ângulo em " + str(functions.tools.entrada_angulo) + ":"), True)
            Tools.voltar()
            
        elif escolha_hipotenusa == "Voltar":
            Tools.clean()
            break


def oposto():
    while True:
        Tools.clean()
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
            Tools.clean()
            oposto_com_hipotenusa(input("Hipotenusa:"), input("Ângulo em " + str(functions.tools.entrada_angulo) + ":"), True)
            Tools.voltar()

        elif escolha_oposto == "Cateto Adjacente":
            Tools.clean()
            oposto_com_adjacente(input("Cateto Adjacente:"), input("Ângulo em " + str(functions.tools.entrada_angulo) + ":"), True)
            Tools.voltar()
        
        elif escolha_oposto == "Voltar":
            Tools.clean()
            break


def adjacente():
    while True:
        Tools.clean()
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
            Tools.clean()
            adjacente_com_hipotenusa(input("Hipotenusa:"), input("Ângulo em " + str(functions.tools.entrada_angulo) + ":"), True)
            Tools.voltar()

        elif escolha_adjacente == "Cateto Oposto":
            Tools.clean()
            adjacente_com_oposto(input("Cateto Adjacente:"), input("Ângulo em " + str(functions.tools.entrada_angulo) + ":"), True)
            Tools.voltar()

        # Voltar
        elif escolha_adjacente == "Voltar":
            Tools.clean()
            break


def angulo():
    while True:
        Tools.clean()
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
            Tools.clean()
            angulo_com_coca(input("Cateto Oposto:"), input("Cateto Adjacente:"), True)
            Tools.voltar()

        elif escolha_angulo == "CO/H":
            Tools.clean()
            angulo_com_coh(input("Cateto Oposto:"), input("Hipotenusa:"), True)
            Tools.voltar()

        elif escolha_angulo == "CA/H":
            Tools.clean()
            angulo_com_cah(input("Cateto Adjacente:"), input("Hipotenusa"), True)
            Tools.voltar()
        
        # Voltar
        elif escolha_angulo == "Voltar":
            Tools.clean()
            break