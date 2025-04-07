from functions.functions import math, trat_erro, resultado, ERROR, calc_expression, euler

def permutacao_n_em_k(n,k, imprimir=False):
    if trat_erro(int, [n, k]):
        n = calc_expression(n, int)
        k = calc_expression(k, int)
        calculo = math.perm(n, k)
        
        resultado("Resultado:", calculo) if imprimir else None
        return calculo


def permutacao_circular(n, imprimir=False):
    if trat_erro(int, [n]):
        n = calc_expression(n, int)
        calculo = math.factorial((n-1))
        
        resultado("Resultado:", calculo) if imprimir else None
        return calculo


def permutacao_caotica(n, imprimir=False):
    if trat_erro(int, [n]):
        n = calc_expression(n, int)
        if n >= 0:
            calculo = math.factorial(n)/euler
            calculoAproximado = int(round(calculo, 0))
            
            resultado("O resultado da permutação caótica é:", calculoAproximado, True) if imprimir else None
            return calculoAproximado
        else:
            ERROR("A quantidade de elementos não pode ser negativa") if imprimir else None


def combinacao(n, p, imprimir=False):
    if trat_erro(int, [n, p]):
        n = calc_expression(n, int)
        p = calc_expression(p, int)
        if n >= 0 and p >= 0:
            calculo = math.factorial(n)/(math.factorial(p) * math.factorial(n-p))

            resultado("Resultado:", calculo) if imprimir else None
            return calculo
        else:
            ERROR("N e P não podem ser negativos") if imprimir else None


def combinacao_completa(n, p, imprimir=False):
    if trat_erro(int, [n, p]):
        n = calc_expression(n, int)
        p = calc_expression(p, int)
        if n >= 0 and p >= 0:
            calculo = math.factorial(n + (p - 1)) / (math.factorial(p) * math.factorial(n - 1))
            
            resultado("Resultado:", calculo, True) if imprimir else None
            return calculo
        else:
            ERROR("N ou P não pode ser negativo") if imprimir else None


def fatorial(value, imprimir=False):
    if trat_erro(int, [value]):
        value = calc_expression(value, int)
        if value >= 0:    
            calculo = math.factorial(value)
            
            resultado("Fatorial desse Número é:", calculo) if imprimir else None
            return calculo
        else:
            ERROR("O número não pode ser negativo") if imprimir else None