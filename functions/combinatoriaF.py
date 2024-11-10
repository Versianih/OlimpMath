from functions.functions import math, tratErro, resultado, ERROR, calcExpression


def PermutaçãoDeNemK(n,k, print=None):
    if tratErro(int, [n, k]) == True:
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        calculo = math.perm(n, k)
        if print == True:
            resultado("Resultado:", calculo)
        return calculo


def PermutaçãoCircular(n, print=None):
    if tratErro(int, [n]) == True:
        n = calcExpression(n, int)
        calculo = math.factorial((n-1))
        if print == True:
            resultado("Resultado:", calculo)
        return calculo


def Combinação(n,k, print=None):
    if tratErro(int, [n, k]) == True:
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        calculo = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
        if print == True:
            resultado("Resultado:", calculo)
        return calculo


def Fatorial(n, print=None):
    if tratErro(int, [n]) == True:
        n = calcExpression(n, int)
        if n >= 0:    
            calculo = math.factorial(n)
            if print == True:
                resultado("Fatorial desse Número é:", calculo)
            return calculo
        else:
            if print == True:
                ERROR("O número não pode ser negativo")
            return None