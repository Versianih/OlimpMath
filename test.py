from functions.algebra import Algebra

sistema_de_equacoes = Algebra.Polinomios.sistema_de_equacoes

# Teste 1: Sistema linear simples com solução única
print("Teste 1")
equacoes1 = ["x + y = 10", "2*x - y = 5"]
solucoes1 = sistema_de_equacoes(equacoes1, imprimir=True)
# Resultado esperado: x = 5, y = 5

# Teste 2: Sistema linear simples com números decimais
print("Teste 2")
equacoes2 = ["2.5*x + 1.5*y = 10", "x - y = 1"]
solucoes2 = sistema_de_equacoes(equacoes2, imprimir=True)
# Resultado esperado: x = 3, y = 2

# Teste 3: Sistema com três variáveis
print("Teste 3")
equacoes3 = ["x + y + z = 6", "2*x - y + z = 7", "x + 2*y - z = 4"]
solucoes3 = sistema_de_equacoes(equacoes3, imprimir=True)
# Resultado esperado: x = 3, y = 2, z = 1

# Teste 4: Sistema não linear simples
print("Teste 4")
equacoes4 = ["x**2 + y**2 = 25", "x + y = 7"]
solucoes4 = sistema_de_equacoes(equacoes4, imprimir=True)
# Resultado esperado: (x=4, y=3) e (x=3, y=4)

# Teste 5: Sistema sem solução
print("Teste 5")
equacoes5 = ["x + y = 5", "x + y = 7"]
solucoes5 = sistema_de_equacoes(equacoes5, imprimir=True)
# Deve retornar None e mostrar mensagem de erro

# Teste 6: Sistema com infinitas soluções
print("Teste 6")
equacoes6 = ["x + y = 10", "2*x + 2*y = 20"]
solucoes6 = sistema_de_equacoes(equacoes6, imprimir=True)
# Resultado pode variar dependendo de como sympy lida com sistemas indeterminados

# Teste 7: Sistema com equações de grau mais alto
print("Teste 7")
equacoes7 = ["x**2 - y = 0", "x - 2 = 0"]
solucoes7 = sistema_de_equacoes(equacoes7, imprimir=True)
# Resultado esperado: x = 2, y = 4

# Teste 8: Sistema com frações
print("Teste 8")
equacoes8 = ["x/2 + y/3 = 4", "x - y = 3"]
solucoes8 = sistema_de_equacoes(equacoes8, imprimir=True)
# Resultado esperado: x = 6, y = 3
