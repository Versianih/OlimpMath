from functions.functions import math, tratErro, resultado, ERROR, calcExpression, euler
from functions.algebraF import Somatório

def PermutaçãoDeNemK(n,k, imprimir=None):
    if tratErro(int, [n, k]):
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        calculo = math.perm(n, k)
        if imprimir:
            resultado("Resultado:", calculo)
        return calculo


def PermutaçãoCircular(n, imprimir=None):
    if tratErro(int, [n]):
        n = calcExpression(n, int)
        calculo = math.factorial((n-1))
        if imprimir:
            resultado("Resultado:", calculo)
        return calculo


def PermutaçãoCaótica(n, imprimir=None):
    if tratErro(int, [n]):
        n = calcExpression(n, int)
        if n >= 0:
            calculo = math.factorial(n)/euler
            calculoAproximado = int(round(calculo, 0))
            if imprimir:
                resultado("O resultado da permutação caótica é:", calculoAproximado, True)
            return calculoAproximado
        else:
            if imprimir:
                ERROR("A quantidade de elementos não pode ser negativa")
            return


def Combinação(n, p, imprimir=None):
    if tratErro(int, [n, p]):
        n = calcExpression(n, int)
        p = calcExpression(p, int)
        if n >= 0 and p >= 0:
            calculo = math.factorial(n)/(math.factorial(p) * math.factorial(n-p))
            if imprimir:
                resultado("Resultado:", calculo)
            return calculo
        else:
            if imprimir:
                ERROR("N e P não podem ser negativos")
            return


def CombinaçãoCompleta(n, p, imprimir=None):
    if tratErro(int, [n, p]):
        n = calcExpression(n, int)
        p = calcExpression(p, int)
        if n >= 0 and p >= 0:
            calculo = math.factorial(n + (p - 1)) / (math.factorial(p) * math.factorial(n - 1))
            if imprimir:
                resultado("Resultado:", calculo, True)
            return calculo
        else:
            if imprimir:
                ERROR("N ou P não pode ser negativo")
            return


def Fatorial(n, imprimir=None):
    if tratErro(int, [n]):
        n = calcExpression(n, int)
        if n >= 0:    
            calculo = math.factorial(n)
            if imprimir:
                resultado("Fatorial desse Número é:", calculo)
            return calculo
        else:
            if imprimir:
                ERROR("O número não pode ser negativo")
            return