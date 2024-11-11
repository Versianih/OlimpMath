from functions.functions import math, tratErro, resultado, ERROR, calcExpression


def Radiciação(a, indice, print=None):
    if tratErro(float, [a]) and tratErro(int, [indice]):
        a = calcExpression(a, float)
        indice = calcExpression(indice, int)    
        calculo = (a)**(1/indice)
        if print == True:
            resultado("Raiz:", calculo, True)
        return calculo


def Exponenciação(a, expoente, print=None):
    if tratErro(float, [a]) and tratErro(int, [expoente]):
        a = calcExpression(a, float)
        expoente = calcExpression(expoente, int)
        calculo = (a)**(expoente)
        if print:
            resultado("Resultado:", calculo, True)
        return calculo
    

def Resto(a, b, print=None):
    if tratErro(float, [a, b]) == True:    
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        calculo = math.remainder(a,b)
        if print == True:
            resultado("Resto:", calculo)
        return calculo
    

def MDC(a,b, print=None):
    if tratErro(int, [a, b]) == True:    
        a = calcExpression(a, int)
        b = calcExpression(b, int)
        calculo = math.gcd(a,b)
        if print == True:
            resultado("MDC:", calculo)
        return calculo
    

def MMC(a, b, print=None):
    if tratErro(int, [a, b]) == True:    
        a = calcExpression(a, int)
        b = calcExpression(b, int)
        calculo = (abs(a*b))/(math.gcd(a,b))
        if print == True:
            resultado("MMC:", calculo)
        return calculo
    

def equação2Grau(a, b, c, print=None):
    if tratErro(float, [a, b, c]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        c = calcExpression(c, float)
        if a != 0:    
            delta = b**2 - (4*a*c)
            if delta >= 0:
                x1 = (-b + (delta**(1/2)))/(2*a)
                x2 = (-b - (delta**(1/2)))/(2*a)
                if print == True:
                    resultado("As Raizes da Equação são:",(x1, x2))
                return [x1, x2]
            else:
                cx1 = (-b + (delta**(1/2)))/(2*a)
                cx2 = (-b - (delta**(1/2)))/(2*a)
                if print == True:
                    resultado("As Raizes Complexas da Equação são:", (cx1, cx2))
                return [cx1, cx2]
        else:
            if print == True:
                ERROR("'a' tem que ser diferente de 0")


def Somatório(n, k, expressao, print=None):
    if tratErro(int, [n, k]) == True:
        somatorio = 0
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        for k in range(k, n + 1):
            somatorio += eval(expressao)
        if print:
            resultado("Resultado do Somatório:", somatorio, True)
        return somatorio
    
    
def Produtório(n, k, expressao, print=None):
    if tratErro(int, [n, k]) == True:
        produtorio = 1
        n = calcExpression(n, int)
        k = calcExpression(k, int)
        for k in range(k, n + 1):
            produtorio *= eval(expressao)
        if print:
            resultado("Resultado do Produtório:", produtorio, True)
        return produtorio


def termoGeralPA(a1, n, r, print=None):
    if tratErro(float, [a1, r]) and tratErro(int, [n]):
        a1 = calcExpression(a1, float)
        r = calcExpression(r, float)
        n = calcExpression(n, int)
        calculo = a1 + ((n-1) * r)
        if print:
            resultado(f"O termo na posição {n} da PA é:", calculo)
        return calculo


def somaPA(a1, an, n, print=None):
    if tratErro(float, [a1, an]) and tratErro(int, [n]):
        a1 = calcExpression(a1, float)
        an = calcExpression(an, float)
        n = calcExpression(n, int)
        calculo = ((a1 + an) * n)/2
        if print:
            resultado(f"A soma dos primeiros {n} termos da PA é:", calculo)
        return calculo
    

def termoGeralPG(a1, n, q, print=None):
    if tratErro(float, [a1, q]) and tratErro(int, [n]):
        a1 = calcExpression(a1, float)
        q = calcExpression(q, float)
        n = calcExpression(n, int)
        calculo = a1 * (q**(n-1))
        if print:
            resultado(f"O termo na posição {n} da PG é:", calculo)
        return calculo


def somaPG(a1, q, n, print=None):
    if tratErro(float, [a1, q]) and tratErro(int, [n]):
        a1 = calcExpression(a1, float)
        q = calcExpression(q, float)
        n = calcExpression(n, int)
        calculo = (a1*((q**n)-1))/(q-1)
        if print:
            resultado(f"A soma dos primeiros {n} termos da PG é:", calculo)
        return calculo