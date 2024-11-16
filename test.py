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



# def resultado(texto, resultado=None, aproximar=None, casas_decimais=2):
#     saida = []
#     if resultado is not None:
#         if isinstance(resultado, list) and aproximar is not None:
#             for res in resultado:
#                     res = round(res, casas_decimais)
#                     saida.append(res)
#             print(GREEN + texto, str(saida) + RESET)
#         elif isinstance(resultado, list) and aproximar is None:
#             print(GREEN + texto, str(resultado) + RESET)
#         else:
#             if aproximar:
#                 resultado = round(resultado, casas_decimais)
#             print(GREEN + texto, str(resultado) + RESET)
#     else:
#         print(GREEN + texto + RESET)
#     print("")


# def get_keypress():
#     try:
#         # Captura a tecla pressionada e tenta decodificar como UTF-8
#         key = msvcrt.getch()
#         decoded_key = key.decode('utf-8') if key else ''
#     except UnicodeDecodeError:
#         # Caso não consiga decodificar como UTF-8, usa ISO-8859-1 como alternativa
#         decoded_key = key.decode('ISO-8859-1') if key else ''
#     return decoded_key
# ola = get_keypress()
# if ola == "\r":
#     print("sucesso")


# import sys

# def get_key():
#     """Captura uma tecla pressionada sem ecoar no terminal."""
#     if sys.platform.startswith("win32"):
#         # Importa apenas para Windows
#         import keyboard
#         event = keyboard.read_event()
#         if event.event_type == keyboard.KEY_DOWN:
#             return event.name
#     elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
#         # Importa apenas para Linux/macOS
#         import termios
#         import tty
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(fd)
#             key = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return key
#     else:
#         raise NotImplementedError("Sistema operacional não suportado!")

# print("Pressione uma tecla (não será exibida):")
# key = get_key()
# print(f"\nVocê pressionou: {key}")