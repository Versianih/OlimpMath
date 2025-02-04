from InquirerPy import prompt
from functions.functions import(
    clean, get_keypress, voltar, acaoInvalida,
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
        elif escolha == "Progressões":
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
                "choices": ["Sistemas", "Segundo Grau", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Sistemas de Equação
        if escolha == "Sistemas":
            clean()
            algebraPolinomiosSistemaEq()
        
        # Equação de Segundo Grau
        elif escolha == "Segundo Grau":
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
        for equacao in equacoes:
            print(GREEN + str(equacao) + RESET)
        print("")
        print(YELLOW + "1) Adicionar Equação")
        print(GREEN + "ENTER) Resolver o Sistema" + RESET)
        escolha = get_keypress()
        
        if escolha == "1":
            clean()
            equacoes.append(input("Equação:"))
        
        elif escolha == "\r":
            clean()
            print(GREEN + "Equações:" + RESET)
            for equacao in equacoes:
                print(YELLOW + str(equacao) + RESET)
            print("")
            print(GREEN + "Soluções do sistema de Equações:" + RESET)
            print("")
            sistemaEq(equacoes, True)
            voltar()
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
        print(GREEN + "TELA INICIAL -> ÁLGEBRA -> PROGRESSÕES -> PA")
        print(YELLOW + "1) Termo Geral da PA")
        print("2) Soma dos primeiros n elementos da PA")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        if escolha == "1":
            clean()
            termoGeralPA(input("Primeiro termo da PA:"), input("Posição do termo que se quer descobrir:"), input("Razão da PA:"), True)
            voltar()
        

        elif escolha == "2":
            clean()
            somaPA(input("Primeiro termo da PA:"), input("Termo n da PA:"), input("Quantidade de elementos na PA:"), True)
            voltar()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def algebraProgressõesPG():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> ÁLGEBRA -> PROGRESSÕES -> PG")
        print(YELLOW + "1) Termo Geral da PG")
        print("2) Soma dos primeiros n elementos da PG")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        if escolha == "1":
            clean()
            termoGeralPG(input("Primeiro termo da PG:"), input("Posição do termo que se quer descobrir:"), input("Razão da PG:"), True)
            voltar()
        

        elif escolha == "2":
            clean()
            somaPG(input("Primeiro termo da PG:"), input("Razão da PG:"), input("Quantidade de elementos da PG:"), True)
            voltar()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()