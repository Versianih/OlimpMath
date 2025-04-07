from InquirerPy import prompt
from functions.functions import(
    clean, voltar, acao_invalida,
    RESET, YELLOW, GREEN,
)

# Básico
from functions.algebraF import(
    radiciacao,
    exponenciacao,
    mdc,
    mmc,
    resto,
    eh_primo,
    fatoracao,
)

# Polinômios
from functions.algebraF import(
    sistema_de_equacoes,
    equacao_segundo_grau,
)

# Progressões
from functions.algebraF import(
    somatorio,
    produtorio,

    termo_geral_pa,
    soma_pa,

    termo_geral_pg, 
    soma_pg,
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
            algebra_basico()

        # Polinômios
        elif escolha == "Polinômios":
            clean()
            algebra_polinomios()

        # Progressões
        elif escolha == "Progressôes":
            clean()
            algebra_progressoes()

        # Sair
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def algebra_basico():
    while True:
        clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA -> BÁSICO",
                "choices": ["Radiciação", "Exponenciação", "MDC", "MMC", "Resto", "É primo?", "Fatoração", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # radiciacao
        if escolha == "Radiciação":
            clean()
            radiciacao(input("Número/Expressão dentro da Raiz:"), input("Índice da Raiz:"), True)
            voltar()

        # exponenciacao
        elif escolha == "Exponenciação":
            clean()
            exponenciacao(input("Base:"), input("Expoente:"), True)
            voltar()

        # mdc
        elif escolha == "MDC":
            clean()
            mdc(input("N₁:"), input("N₂:"), True)
            voltar()

        # mmc
        elif escolha == "MMC":
            clean()
            mmc(input("N₁:"), input("N₂:"), True)
            voltar()

        # resto
        elif escolha == "Resto":
            clean()
            resto(input("Dividendo:"), input("Divisor:"), True)
            voltar()

        # É primo
        elif escolha == "É primo?":
            clean()
            eh_primo(input("Número que deseja verificar se é primo:"), True)
            voltar()

        # Fatoração
        elif escolha == "Fatoração":
            clean()
            fatoracao(input("Número a ser fatorado:"), True)
            voltar()
            
        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def algebra_polinomios():
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
            algebra_polinomios_sistema_de_equacoes()
        
        # Equação de Segundo Grau
        elif escolha == "Equação do Segundo Grau":
            clean()
            equacao_segundo_grau(input("a:"), input("b:"), input("c:"), True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def algebra_polinomios_sistema_de_equacoes():
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
            sistema_de_equacoes(equacoes, True)
            voltar()
            break

        elif escolha == "Sair":
            clean()
            break
        else:
            acao_invalida()


def algebra_progressoes():
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

        # somatorio
        if escolha == "Somatório":
            clean()
            somatorio(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        # produtorio
        elif escolha == "Produtório":
            clean()
            produtorio(input("n:"), input("k:"), input("Expressão:"), True)
            voltar()

        # PA
        elif escolha == "PA":
            clean()
            algebra_progressoes_pa()

        # PG
        elif escolha == "PG":
            clean()
            algebra_progressoes_pg()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def algebra_progressoes_pa():
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
            termo_geral_pa(input("Primeiro termo da PA:"), input("Posição do termo que se quer descobrir:"), input("Razão da PA:"), True)
            voltar()
        

        elif escolha == "Soma de n elementos da PA":
            clean()
            soma_pa(input("Primeiro termo da PA:"), input("Termo n da PA:"), input("Quantidade de elementos na PA:"), True)
            voltar()

        # Sair
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def algebra_progressoes_pg():
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
            termo_geral_pg(input("Primeiro termo da PG:"), input("Posição do termo que se quer descobrir:"), input("Razão da PG:"), True)
            voltar()
        

        elif escolha == "Soma de n elementos da PG":
            clean()
            soma_pg(input("Primeiro termo da PG:"), input("Razão da PG:"), input("Quantidade de elementos da PG:"), True)
            voltar()

        # Sair
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()