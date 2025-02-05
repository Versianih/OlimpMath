from InquirerPy import prompt
from functions.functions import(
    clean, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,
)

# Básico
from functions.algebraF import(
    Radiciação,
    Exponenciação,
    MDC,
    MMC,
    Resto,
)

# Polinômios
from functions.algebraF import(
    sistemaEq,
    equação2Grau,
)

# Progressões
from functions.algebraF import(
    Somatório,
    Produtório,

    termoGeralPA,
    somaPA,

    termoGeralPG, 
    somaPG,
)


def algebra():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA",
                "choices": ["Básico", "Polinômios", "Progressôes", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)
        
        # Básico
        if escolha == "Básico":
            clean()
            algebraBásico()

        # Polinômios
        elif escolha == "Polinômios":
            clean()
            algebraPolinomios()

        # Progressões
        elif escolha == "Progressôes":
            clean()
            algebraProgressões()

        # Sair
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def algebraBásico():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA -> BÁSICO",
                "choices": ["Radiciação", "Exponenciação", "MDC", "MMC", "Resto", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Radiciação
        if escolha == "Radiciação":
            clean()
            Radiciação(input("Número/Expressão dentro da Raiz:"), input("Índice da Raiz:"), True)
            voltar()

        # Exponenciação
        elif escolha == "Exponenciação":
            clean()
            Exponenciação(input("Base:"), input("Expoente:"), True)
            voltar()

        # MDC
        elif escolha == "MDC":
            clean()
            MDC(input("N₁:"), input("N₂:"), True)
            voltar()

        # MMC
        elif escolha == "MMC":
            clean()
            MMC(input("N₁:"), input("N₂:"), True)
            voltar()

        # Resto
        elif escolha == "Resto":
            clean()
            Resto(input("Dividendo:"), input("Divisor:"), True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def algebraPolinomios():
    while True: 
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA -> POLINÔMIOS",
                "choices": ["Sistemas de Equações", "Equação do Segundo Grau", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Sistemas de Equação
        if escolha == "Sistemas de Equações":
            clean()
            algebraPolinomiosSistemaEq()
        
        # Equação de Segundo Grau
        elif escolha == "Equação do Segundo Grau":
            clean()
            equação2Grau(input("a:"), input("b:"), input("c:"), True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def algebraPolinomiosSistemaEq():
    equacoes = []
    while True:
        clean()
        print(YELLOW + "Equações:" + RESET)
        for i, equacao in enumerate(equacoes):
            print(GREEN + f"Equação {i+1}: {equacao}" + RESET)
        print("")
        campos = [
            {
                "type": "list",
                "message": "SELECIONE UMA AÇÃO",
                "choices": ["Adicionar Equação", "Salvar e Resolver o Sistema", "Sair"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)
        
        if escolha == "Adicionar Equação":
            clean()
            equacoes.append(input("Equação:"))
        
        elif escolha == "Salvar e Resolver o Sistema":
            clean()
            print(GREEN + "Equações:" + RESET)
            for i, equacao in enumerate(equacoes):
                print(GREEN + f"Equação {i+1}: {equacao}" + RESET)
            print("")
            print(GREEN + "Soluções do sistema de Equações:" + RESET)
            print("")
            sistemaEq(equacoes, True)
            voltar()
            break

        elif escolha == "Sair":
            clean()
            break
        else:
            acaoInvalida()


def algebraProgressões():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA -> PROGRESSÕES",
                "choices": ["Somatório", "Produtório", "PA", "PG", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Somatório
        if escolha == "Somatório":
            clean()
            Somatório(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        # Produtório
        elif escolha == "Produtório":
            clean()
            Produtório(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        # PA
        elif escolha == "PA":
            clean()
            algebraProgressõesPA()

        # PG
        elif escolha == "PG":
            clean()
            algebraProgressõesPG()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def algebraProgressõesPA():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA -> PROGRESSÕES -> PA",
                "choices": ["Termo Geral da PA", "Soma de n elementos da PA", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        if escolha == "Termo Geral da PA":
            clean()
            termoGeralPA(input("Primeiro termo da PA:"), input("Posição do termo que se quer descobrir:"), input("Razão da PA:"), True)
            voltar()
        

        elif escolha == "Soma de n elementos da PA":
            clean()
            somaPA(input("Primeiro termo da PA:"), input("Termo n da PA:"), input("Quantidade de elementos na PA:"), True)
            voltar()

        # Sair
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def algebraProgressõesPG():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA -> PROGRESSÕES -> PG",
                "choices": ["Termo Geral da PG", "Soma de n elementos da PG", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)


        if escolha == "Termo Geral da PG":
            clean()
            termoGeralPG(input("Primeiro termo da PG:"), input("Posição do termo que se quer descobrir:"), input("Razão da PG:"), True)
            voltar()
        

        elif escolha == "Soma de n elementos da PG":
            clean()
            somaPG(input("Primeiro termo da PG:"), input("Razão da PG:"), input("Quantidade de elementos da PG:"), True)
            voltar()

        # Sair
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()