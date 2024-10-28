from functions.functions import math, tratErro, resultado, ERROR


def PermutaçãoDeNemK(n,k):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)    
        calculo = math.perm(n, k)
        return resultado("Resultado: " + str(calculo))


def PermutaçãoCircular(n):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial((n-1))
        return resultado("Resultado: " + str(calculo))


def Combinação(n,k):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)
        calculo = math.comb(n,k)
        return resultado("Resultado: " + str(calculo))


def Fatorial(n):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial(n)
        return resultado("Fatorial desse Número é: " + str(calculo))