from sympy import symbols, Eq, solve

# Definindo variáveis simbólicas
x = symbols('x')
y = symbols('y')
z = symbols('z')

# Definindo a equação
equacao = Eq(x**2 - y, 0)

# Resolvendo a equação
solucoes = solve(equacao, x)
print("Soluções para (x, y):", solucoes)