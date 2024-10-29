from functions.functions import math, tratErro, resultado, ERROR


def PermutaçãoDeNemK(n,k):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)    
        calculo = math.perm(n, k)
        resultado("Resultado: " + str(calculo))
        return calculo


def PermutaçãoCircular(n):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial((n-1))
        resultado("Resultado: " + str(calculo))
        return calculo


def Combinação(n,k):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)
        calculo = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
        resultado("Resultado: " + str(calculo))
        return calculo


def Fatorial(n):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial(n)
        resultado("Fatorial desse Número é: " + str(calculo))
        return calculo