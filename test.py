from sympy import symbols, pi, Rational, nsimplify, simplify

# Definir símbolo
r = symbols('r')

# Raio como número decimal
raio_decimal = 2.5

# Converter para fração exata
raio_fracao = nsimplify(raio_decimal)

# Calcular área do círculo
area_circulo = pi * raio_fracao**2

# Simplificar a expressão
resultado_final = simplify(area_circulo)

print("Área do Círculo:", resultado_final)