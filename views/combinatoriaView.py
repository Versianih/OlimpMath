from InquirerPy import prompt
from functions.tools import(
    Tools,
    RESET, RED, YELLOW, GREEN,
)
from functions.combinatoriaF import Combinatoria


def combinatoria():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "COMBINATÓRIA",
                "choices": ["Combinação (N P)", "Combinação Completa (N P)", "Permutação N em K", "Permutação Circular", "Permutação Caótica", "Fatorial", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Combinação
        if escolha == "Combinação (N P)":
            Tools.clean()
            Combinatoria.Combinacao.combinacao(input("Insira N:"), input("Insira P:"), imprimir=True)
            Tools.voltar()
        
        # Combinação Completa
        elif escolha == "Combinação Completa (N P)":
            Tools.clean()
            Combinatoria.Combinacao.combinacao_completa(input("Insira N:"), input("Insira P:"), imprimir=True)
            Tools.voltar()

        # Permutação
        elif escolha == "Permutação N em K":
            Tools.clean()
            Combinatoria.Permutacao.permutacao_n_em_k(input("Insira N:"), input("Insira K:"), imprimir=True)
            Tools.voltar()
        
        # Permutação Circular
        elif escolha == "Permutação Circular":
            Tools.clean()
            Combinatoria.Permutacao.permutacao_circular(input("Número de Elementos: "), imprimir=True)
            Tools.voltar()
        
        # Permutação Caótica
        elif escolha == "Permutação Caótica":
            Tools.clean()
            Combinatoria.Permutacao.permutacao_caotica(input("Quantidade de Elementos:"), imprimir=True)
            Tools.voltar()
            
        # Fatorial
        elif escolha == "Fatorial":
            Tools.clean()
            Combinatoria.fatorial(input("Número:"), imprimir=True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break