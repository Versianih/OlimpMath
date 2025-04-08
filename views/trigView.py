from InquirerPy import prompt
from functions.tools import(
    Tools,
    RESET, RED, YELLOW, GREEN,
)
from functions.trigF import Trigonometria


def trig(ENTRADA_ANGULO, SAIDA_ANGULO):
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TRIGONOMETRIA",
                "choices": ["Calcular Hipotenusa +", "Calcular Cateto Oposto +", "Calcular Cateto Adjacente +", "Calcular Ângulo +", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == "Calcular Hipotenusa +":
            hipotenusa(ENTRADA_ANGULO)

        elif escolha == "Calcular Cateto Oposto +":
            oposto(ENTRADA_ANGULO)
        
        elif escolha == "Calcular Cateto Adjacente +":
            adjacente(ENTRADA_ANGULO)

        elif escolha == "Calcular Ângulo +":
            angulo(SAIDA_ANGULO)

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def hipotenusa(ENTRADA_ANGULO):
    while True:
        Tools.clean()
        campos_hipotenusa = [
            {
                "type": "list",
                "message": "TRIGONOMETRIA -> HIPOTENUSA",
                "choices": ["Cateto Oposto", "Cateto Adjacente", "Voltar"],
            }
        ]
        escolha_hipotenusa = prompt(campos_hipotenusa)
        escolha_hipotenusa = escolha_hipotenusa.get(0)

        if escolha_hipotenusa == "Cateto Oposto":
            Tools.clean()
            Trigonometria.Hipotenusa.com_oposto(input("Cateto Oposto:"), input(f"Ângulo em {ENTRADA_ANGULO}:"), ENTRADA_ANGULO, True)
            Tools.voltar()

        elif escolha_hipotenusa == "Cateto Adjacente":
            Tools.clean()
            Trigonometria.Hipotenusa.com_adjacente(input("Cateto Adjacente:"), input(f"Ângulo em {ENTRADA_ANGULO}:"), ENTRADA_ANGULO, True)
            Tools.voltar()
            
        elif escolha_hipotenusa == "Voltar":
            Tools.clean()
            break


def oposto(ENTRADA_ANGULO):
    while True:
        Tools.clean()
        campos_oposto = [
            {
                "type": "list",
                "message": "TRIGONOMETRIA -> CATETO OPOSTO",
                "choices": ["Hipotenusa", "Cateto Adjacente", "Voltar"],
            }
        ]
        escolha_oposto = prompt(campos_oposto)
        escolha_oposto = escolha_oposto.get(0)

        
        if escolha_oposto == "Hipotenusa":
            Tools.clean()
            Trigonometria.Oposto.com_hipotenusa(input("Hipotenusa:"), input(f"Ângulo em {ENTRADA_ANGULO}:"), ENTRADA_ANGULO, True)
            Tools.voltar()

        elif escolha_oposto == "Cateto Adjacente":
            Tools.clean()
            Trigonometria.Oposto.com_adjacente(input("Cateto Adjacente:"), input(f"Ângulo em {ENTRADA_ANGULO}:"), ENTRADA_ANGULO, True)
            Tools.voltar()
        
        elif escolha_oposto == "Voltar":
            Tools.clean()
            break


def adjacente(ENTRADA_ANGULO):
    while True:
        Tools.clean()
        campos_adjacente = [
            {
                "type": "list",
                "message": "TRIGONOMETRIA -> ADJACENTE",
                "choices": ["Hipotenusa", "Cateto Oposto", "Voltar"],
            }
        ]
        escolha_adjacente = prompt(campos_adjacente)
        escolha_adjacente = escolha_adjacente.get(0)

        
        if escolha_adjacente == "Hipotenusa":
            Tools.clean()
            Trigonometria.Adjacente.com_hipotenusa(input("Hipotenusa:"), input(f"Ângulo em {ENTRADA_ANGULO}:"), ENTRADA_ANGULO, True)
            Tools.voltar()

        elif escolha_adjacente == "Cateto Oposto":
            Tools.clean()
            Trigonometria.Adjacente.com_oposto(input("Cateto Adjacente:"), input(f"Ângulo em {ENTRADA_ANGULO}:"), ENTRADA_ANGULO, True)
            Tools.voltar()

        # Voltar
        elif escolha_adjacente == "Voltar":
            Tools.clean()
            break


def angulo(SAIDA_ANGULO):
    while True:
        Tools.clean()
        campos_angulo = [
            {
                "type": "list",
                "message": "TRIGONOMETRIA -> ÂNGULO",
                "choices": ["CO/CA", "CO/H", "CA/H", "Voltar"],
            }
        ]
        escolha_angulo = prompt(campos_angulo)
        escolha_angulo = escolha_angulo.get(0)

        if escolha_angulo == "CO/CA":
            Tools.clean()
            Trigonometria.Angulo.com_coca(input("Cateto Oposto:"), input("Cateto Adjacente:"), SAIDA_ANGULO, True)
            Tools.voltar()

        elif escolha_angulo == "CO/H":
            Tools.clean()
            Trigonometria.Angulo.com_coh(input("Cateto Oposto:"), input("Hipotenusa:"), SAIDA_ANGULO, True)
            Tools.voltar()

        elif escolha_angulo == "CA/H":
            Tools.clean()
            Trigonometria.Angulo.com_cah(input("Cateto Adjacente:"), input("Hipotenusa"), SAIDA_ANGULO, True)
            Tools.voltar()
        
        # Voltar
        elif escolha_angulo == "Voltar":
            Tools.clean()
            break