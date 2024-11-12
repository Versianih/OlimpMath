from functions.functions import math, tratErro, resultado, ERROR, calcExpression


def PermutaçãoDeNemK(n,k, imprimir=None):
    if tratErro(int, [n, k]) == True:
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        calculo = math.perm(n, k)
        if imprimir == True:
            resultado("Resultado:", calculo)
        return calculo


def PermutaçãoCircular(n, imprimir=None):
    if tratErro(int, [n]) == True:
        n = calcExpression(n, int)
        calculo = math.factorial((n-1))
        if imprimir == True:
            resultado("Resultado:", calculo)
        return calculo


def Combinação(n,k, imprimir=None):
    if tratErro(int, [n, k]) == True:
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        calculo = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
        if imprimir == True:
            resultado("Resultado:", calculo)
        return calculo


def Fatorial(n, imprimir=None):
    if tratErro(int, [n]) == True:
        n = calcExpression(n, int)
        if n >= 0:    
            calculo = math.factorial(n)
            if imprimir == True:
                resultado("Fatorial desse Número é:", calculo)
            return calculo
        else:
            if imprimir == True:
                ERROR("O número não pode ser negativo")
            return None