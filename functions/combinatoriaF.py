from functions.functions import math, tratErro, resultado


def PermutaçãoDeNemK(n,k, print=None):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)    
        calculo = math.perm(n, k)
        if print == True:
            resultado("Resultado:", calculo)
        return calculo


def PermutaçãoCircular(n, print=None):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial((n-1))
        if print == True:
            resultado("Resultado:", calculo)
        return calculo


def Combinação(n,k, print=None):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)
        calculo = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
        if print == True:
            resultado("Resultado:", calculo)
        return calculo


def Fatorial(n, print=None):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial(n)
        if print == True:
            resultado("Fatorial desse Número é:", calculo)
        return calculo