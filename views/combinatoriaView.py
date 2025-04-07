from InquirerPy import prompt
from functions.functions import(
    clean, voltar, acao_invalida,
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
        clean()
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
            clean()
            combinacao(input("Insira N:"), input("Insira P:"), imprimir=True)
            voltar()
        
        # Combinação Completa
        elif escolha == "Combinação Completa (N P)":
            clean()
            combinacao_completa(input("Insira N:"), input("Insira P:"), imprimir=True)
            voltar()

        # Permutação
        elif escolha == "Permutação N em K":
            clean()
            permutacao_n_em_k(input("Insira N:"), input("Insira K:"), imprimir=True)
            voltar()
        
        # Permutação Circular
        elif escolha == "Permutação Circular":
            clean()
            permutacao_circular(input("Número de Elementos: "), imprimir=True)
            voltar()
        
        # Permutação Caótica
        elif escolha == "Permutação Caótica":
            clean()
            permutacao_caotica(input("Quantidade de Elementos:"), imprimir=True)
            voltar()
            
        # Fatorial
        elif escolha == "Fatorial":
            clean()
            fatorial(input("Número:"), imprimir=True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()