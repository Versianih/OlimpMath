from functions.functions import math, tratErro, resultado, ERROR, calcExpression, euler
from functions.algebraF import Somatório

def PermutaçãoDeNemK(n,k, imprimir=None):
    if tratErro(int, [n, k]):
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        calculo = math.perm(n, k)
        
        resultado("Resultado:", calculo) if imprimir else None
        return calculo


def PermutaçãoCircular(n, imprimir=None):
    if tratErro(int, [n]):
        n = calcExpression(n, int)
        calculo = math.factorial((n-1))
        
        resultado("Resultado:", calculo) if imprimir else None
        return calculo


def PermutaçãoCaótica(n, imprimir=None):
    if tratErro(int, [n]):
        n = calcExpression(n, int)
        if n >= 0:
            calculo = math.factorial(n)/euler
            calculoAproximado = int(round(calculo, 0))
            
            resultado("O resultado da permutação caótica é:", calculoAproximado, True) if imprimir else None
            return calculoAproximado
        else:
            ERROR("A quantidade de elementos não pode ser negativa") if imprimir else None


def Combinação(n, p, imprimir=None):
    if tratErro(int, [n, p]):
        n = calcExpression(n, int)
        p = calcExpression(p, int)
        if n >= 0 and p >= 0:
            calculo = math.factorial(n)/(math.factorial(p) * math.factorial(n-p))

            resultado("Resultado:", calculo) if imprimir else None
            return calculo
        else:
            ERROR("N e P não podem ser negativos") if imprimir else None


def CombinaçãoCompleta(n, p, imprimir=None):
    if tratErro(int, [n, p]):
        n = calcExpression(n, int)
        p = calcExpression(p, int)
        if n >= 0 and p >= 0:
            calculo = math.factorial(n + (p - 1)) / (math.factorial(p) * math.factorial(n - 1))
            
            resultado("Resultado:", calculo, True) if imprimir else None
            return calculo
        else:
            ERROR("N ou P não pode ser negativo") if imprimir else None


def Fatorial(value, imprimir=None):
    if tratErro(int, [value]):
        value = calcExpression(value, int)
        if value >= 0:    
            calculo = math.factorial(value)
            
            resultado("Fatorial desse Número é:", calculo) if imprimir else None
            return calculo
        else:
            ERROR("O número não pode ser negativo") if imprimir else None