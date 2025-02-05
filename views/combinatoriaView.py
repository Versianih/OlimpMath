from InquirerPy import prompt
from functions.functions import(
    clean, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,
)
from functions.combinatoriaF import(
    Combinação,
    CombinaçãoCompleta,
    PermutaçãoDeNemK,
    PermutaçãoCircular,
    PermutaçãoCaótica,
    Fatorial,
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
            Combinação(input("Insira N:"), input("Insira P:"), imprimir=True)
            voltar()
        
        # Combinação Completa
        elif escolha == "Combinação Completa (N P)":
            clean()
            CombinaçãoCompleta(input("Insira N:"), input("Insira P:"), imprimir=True)
            voltar()

        # Permutação
        elif escolha == "Permutação N em K":
            clean()
            PermutaçãoDeNemK(input("Insira N:"), input("Insira K:"), imprimir=True)
            voltar()
        
        # Permutação Circular
        elif escolha == "Permutação Circular":
            clean()
            PermutaçãoCircular(input("Número de Elementos: "), imprimir=True)
            voltar()
        
        # Permutação Caótica
        elif escolha == "Permutação Caótica":
            clean()
            PermutaçãoCaótica(input("Quantidade de Elementos:"), imprimir=True)
            voltar()
            
        # Fatorial
        elif escolha == "Fatorial":
            clean()
            Fatorial(input("Número:"), imprimir=True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()