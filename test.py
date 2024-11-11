import msvcrt
# from sympy import symbols, Eq, solve, sympify

# def sistemaEq(equacoes, prin=None):
#     equacoes = [sympify(eq) for eq in equacoes]    
#     variaveis = sorted({str(simbolo) for eq in equacoes for simbolo in eq.free_symbols})
#     variaveis = symbols(variaveis)
#     sistema_equacoes = [Eq(eq, 0) for eq in equacoes]
    
#     solucoes = solve(sistema_equacoes, variaveis)
    
#     if prin:
#         for variavel, valor in solucoes.items():
#             print(f"{variavel} = {valor}")
#     return solucoes

# # Exemplo de uso
# # Definindo um sistema de três equações como strings
# equacoes = [
#     "a + b + c - 6",   # a + b + c = 6
#     "2*a + b - c - 3", # 2a + b - c = 3
#     "a - b + c - 2"    # a - b + c = 2
# ]

# # Resolvendo o sistema
# sistemaEq(equacoes, True)


def get_keypress():
    try:
        # Captura a tecla pressionada e tenta decodificar como UTF-8
        key = msvcrt.getch()
        decoded_key = key.decode('utf-8') if key else ''
    except UnicodeDecodeError:
        # Caso não consiga decodificar como UTF-8, usa ISO-8859-1 como alternativa
        decoded_key = key.decode('ISO-8859-1') if key else ''
    return decoded_key
ola = get_keypress()
if ola == "\r":
    print("sucesso")