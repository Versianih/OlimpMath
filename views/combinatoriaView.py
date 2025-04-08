from InquirerPy import prompt
from functions.tools import(
    Tools,
    RESET, RED, YELLOW, GREEN,
)
from functions.combinatoriaF import(
    combinacao,
    combinacao_completa,
    permutacao_n_em_k,
    permutacao_circular,
    permutacao_caotica,
    fatorial,
)


def combinatoria():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> COMBINATÓRIA",
                "choices": ["Combinação (N P)", "Combinação Completa (N P)", "Permutação N em K", "Permutação Circular", "Permutação Caótica", "Fatorial", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Combinação
        if escolha == "Combinação (N P)":
            Tools.clean()
            combinacao(input("Insira N:"), input("Insira P:"), imprimir=True)
            Tools.voltar()
        
        # Combinação Completa
        elif escolha == "Combinação Completa (N P)":
            Tools.clean()
            combinacao_completa(input("Insira N:"), input("Insira P:"), imprimir=True)
            Tools.voltar()

        # Permutação
        elif escolha == "Permutação N em K":
            Tools.clean()
            permutacao_n_em_k(input("Insira N:"), input("Insira K:"), imprimir=True)
            Tools.voltar()
        
        # Permutação Circular
        elif escolha == "Permutação Circular":
            Tools.clean()
            permutacao_circular(input("Número de Elementos: "), imprimir=True)
            Tools.voltar()
        
        # Permutação Caótica
        elif escolha == "Permutação Caótica":
            Tools.clean()
            permutacao_caotica(input("Quantidade de Elementos:"), imprimir=True)
            Tools.voltar()
            
        # Fatorial
        elif escolha == "Fatorial":
            Tools.clean()
            fatorial(input("Número:"), imprimir=True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break