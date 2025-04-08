from InquirerPy import prompt
from functions.tools import(
    Tools,
    RESET, YELLOW, GREEN,
)

from functions.algebraF import Algebra

def algebra():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> ÁLGEBRA",
                "choices": ["Básico", "Polinômios", "Progressões", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)
        
        # Básico
        if escolha == "Básico":
            Tools.clean()
            algebra_basico()

        # Polinômios
        elif escolha == "Polinômios":
            Tools.clean()
            algebra_polinomios()

        # Progressões
        elif escolha == "Progressões":
            Tools.clean()
            algebra_progressoes()

        # Sair
        elif escolha == "Voltar":
            Tools.clean()
            break


def algebra_basico():
    while True:
        Tools.clean()
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
            Tools.clean()
            Algebra.Basico.radiciacao(input("Número/Expressão dentro da Raiz:"), input("Índice da Raiz:"), True)
            Tools.voltar()

        # exponenciacao
        elif escolha == "Exponenciação":
            Tools.clean()
            Algebra.Basico.exponenciacao(input("Base:"), input("Expoente:"), True)
            Tools.voltar()

        # mdc
        elif escolha == "MDC":
            Tools.clean()
            Algebra.Basico.mdc(input("N₁:"), input("N₂:"), True)
            Tools.voltar()

        # mmc
        elif escolha == "MMC":
            Tools.clean()
            Algebra.Basico.mmc(input("N₁:"), input("N₂:"), True)
            Tools.voltar()

        # resto
        elif escolha == "Resto":
            Tools.clean()
            Algebra.Basico.resto(input("Dividendo:"), input("Divisor:"), True)
            Tools.voltar()

        # É primo
        elif escolha == "É primo?":
            Tools.clean()
            Algebra.Basico.eh_primo(input("Número que deseja verificar se é primo:"), True)
            Tools.voltar()

        # Fatoração
        elif escolha == "Fatoração":
            Tools.clean()
            Algebra.Basico.fatoracao(input("Número a ser fatorado:"), True)
            Tools.voltar()
            
        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def algebra_polinomios():
    while True: 
        Tools.clean()
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
            Tools.clean()
            algebra_polinomios_sistema_de_equacoes()
        
        # Equação de Segundo Grau
        elif escolha == "Equação do Segundo Grau":
            Tools.clean()
            Algebra.Polinomios.equacao_segundo_grau(input("a:"), input("b:"), input("c:"), True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def algebra_polinomios_sistema_de_equacoes():
    equacoes = []
    while True:
        Tools.clean()
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
            Tools.clean()
            equacoes.append(input("Equação:"))
        
        elif escolha == "Salvar e Resolver o Sistema":
            Tools.clean()
            print(GREEN + "Equações:" + RESET)
            for i, equacao in enumerate(equacoes):
                print(GREEN + f"Equação {i+1}: {equacao}" + RESET)
            print("")
            print(GREEN + "Soluções do sistema de Equações:" + RESET)
            print("")
            Algebra.Polinomios.sistema_de_equacoes(equacoes, True)
            Tools.voltar()
            break

        elif escolha == "Sair":
            Tools.clean()
            break


def algebra_progressoes():
    while True:
        Tools.clean()
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
            Tools.clean()
            Algebra.Progressoes.somatorio(input("n:"), input("k:"), input("Expressão:"), True)
            Tools.voltar()

        # produtorio
        elif escolha == "Produtório":
            Tools.clean()
            Algebra.Progressoes.produtorio(input("n:"), input("k:"), input("Expressão:"), True)
            Tools.voltar()

        # PA
        elif escolha == "PA":
            Tools.clean()
            algebra_progressoes_pa()

        # PG
        elif escolha == "PG":
            Tools.clean()
            algebra_progressoes_pg()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def algebra_progressoes_pa():
    while True:
        Tools.clean()
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
            Tools.clean()
            Algebra.Progressoes.termo_geral_pa(input("Primeiro termo da PA:"), input("Posição do termo que se quer descobrir:"), input("Razão da PA:"), True)
            Tools.voltar()
        

        elif escolha == "Soma de n elementos da PA":
            Tools.clean()
            Algebra.Progressoes.soma_pa(input("Primeiro termo da PA:"), input("Termo n da PA:"), input("Quantidade de elementos na PA:"), True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def algebra_progressoes_pg():
    while True:
        Tools.clean()
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
            Tools.clean()
            Algebra.Progressoes.termo_geral_pg(input("Primeiro termo da PG:"), input("Posição do termo que se quer descobrir:"), input("Razão da PG:"), True)
            Tools.voltar()
        

        elif escolha == "Soma de n elementos da PG":
            Tools.clean()
            Algebra.Progressoes.soma_pg(input("Primeiro termo da PG:"), input("Razão da PG:"), input("Quantidade de elementos da PG:"), True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break