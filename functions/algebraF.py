from sympy import symbols, Eq, solve, sympify
from functions.functions import math, trat_erro, resultado, ERROR, calc_expression


def radiciacao(a, indice, imprimir=False):
    if trat_erro(float, [a]) and trat_erro(int, [indice]):
        a = calc_expression(a, float)
        indice = calc_expression(indice, int)    
        calculo = (a)**(1/indice)

        resultado("Raiz:", calculo, aproximar=True) if imprimir else None
        return calculo


def exponenciacao(a, expoente, imprimir=False):
    if trat_erro(float, [a]) and trat_erro(int, [expoente]):
        a = calc_expression(a, float)
        expoente = calc_expression(expoente, int)
        calculo = (a)**(expoente)

        resultado("Resultado:", calculo, aproximar=True) if imprimir else None
        return calculo
    

def resto(a, b, imprimir=False):
    if trat_erro(float, [a, b]):    
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        calculo = math.remainder(a,b)

        resultado("Resto:", calculo) if imprimir else None
        return calculo
    

def mdc(a,b, imprimir=False):
    if trat_erro(int, [a, b]):    
        a = calc_expression(a, int)
        b = calc_expression(b, int)
        calculo = math.gcd(a,b)

        resultado("MDC:", calculo) if imprimir else None
        return calculo
    

def mmc(a, b, imprimir=False):
    if trat_erro(int, [a, b]):    
        a = calc_expression(a, int)
        b = calc_expression(b, int)
        calculo = (abs(a*b))/(math.gcd(a,b))

        resultado("MMC:", calculo) if imprimir else None
        return calculo


def fatoracao(n, imprimir=False):
    if trat_erro(int, [n]):
        n = calc_expression(n, int)
        n_perm = n
        primfac = []
        d = 2
        while d*d <= n:
            while (n % d) == 0:
                primfac.append(d)
                n //= d
            d += 1
        if n > 1:
            primfac.append(n)

        resultado(f"A fatoração de {n_perm} em fatores primos é: {primfac}") if imprimir else None
        return primfac


def sistema_de_equacoes(equacoesStr, imprimir=False):
    if not equacoesStr:
        ERROR("Erro: A lista de equações está vazia!")
        return
    equacoes = []
    for eq in equacoesStr:
        try:
            eq_simbolica = Eq(sympify(eq.split('=')[0]), sympify(eq.split('=')[1]))
            equacoes.append(eq_simbolica)
        except Exception as e:
            ERROR(f"Erro ao processar a equação: {eq}. Erro: {str(e)}")
            return
    variaveis = sorted({str(simbolo) for eq in equacoes for simbolo in eq.free_symbols})    
    variaveis = symbols(variaveis)
    try:
        solucoes = solve(equacoes, variaveis)
    except Exception as e:
        ERROR(f"Erro ao resolver o sistema: {str(e)}")
        return
        
    if imprimir:
        for variavel, valor in solucoes.items():
            resultado(f"{variavel} = {valor}")
    return solucoes


def equacao_segundo_grau(a, b, c, imprimir=False):
    if trat_erro(float, [a, b, c]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        c = calc_expression(c, float)
        if a != 0:    
            delta = b**2 - (4*a*c)
            if delta >= 0:
                x1 = (-b + (delta**(1/2)))/(2*a)
                x2 = (-b - (delta**(1/2)))/(2*a)

                resultado("X1:", x1, aproximar=True) if imprimir else None
                resultado("X2:", x2, aproximar=True) if imprimir else None
                return [x1, x2]
            else:
                cx1 = (-b + (delta**(1/2)))/(2*a)
                cx2 = (-b - (delta**(1/2)))/(2*a)

                resultado("X1:", cx1, aproximar=True) if imprimir else None
                resultado("X2:", cx2, aproximar=True) if imprimir else None
                return [cx1, cx2]
        else:
            ERROR("'a' tem que ser diferente de 0") if imprimir else None


def somatorio(n, k, expressao, imprimir=False):
    if trat_erro(int, [n, k]):
        somatorio = 0
        n = calc_expression(n, int)
        k = calc_expression(k, int)
        for k in range(k, n + 1):
            somatorio += eval(expressao)

        resultado("Resultado do Somatório:", somatorio, aproximar=True) if imprimir else None
        return somatorio
    
    
def produtorio(n, k, expressao, imprimir=False):
    if trat_erro(int, [n, k]):
        produtorio = 1
        n = calc_expression(n, int)
        k = calc_expression(k, int)
        for k in range(k, n + 1):
            produtorio *= eval(expressao)

        resultado("Resultado do Produtório:", produtorio, aproximar=True) if imprimir else None
        return produtorio


def termo_geral_pa(a1, n, r, imprimir=False):
    if trat_erro(float, [a1, r]) and trat_erro(int, [n]):
        a1 = calc_expression(a1, float)
        r = calc_expression(r, float)
        n = calc_expression(n, int)
        calculo = a1 + ((n-1) * r)

        resultado(f"O termo na posição {n} da PA é:", calculo) if imprimir else None
        return calculo


def soma_pa(a1, an, n, imprimir=False):
    if trat_erro(float, [a1, an]) and trat_erro(int, [n]):
        a1 = calc_expression(a1, float)
        an = calc_expression(an, float)
        n = calc_expression(n, int)
        calculo = ((a1 + an) * n)/2

        resultado(f"A soma dos primeiros {n} termos da PA é:", calculo) if imprimir else None
        return calculo
    

def termo_geral_pg(a1, n, q, imprimir=False):
    if trat_erro(float, [a1, q]) and trat_erro(int, [n]):
        a1 = calc_expression(a1, float)
        q = calc_expression(q, float)
        n = calc_expression(n, int)
        calculo = a1 * (q**(n-1))

        resultado(f"O termo na posição {n} da PG é:", calculo) if imprimir else None
        return calculo


def soma_pg(a1, q, n, imprimir=False):
    if trat_erro(float, [a1, q]) and trat_erro(int, [n]):
        a1 = calc_expression(a1, float)
        q = calc_expression(q, float)
        n = calc_expression(n, int)
        calculo = (a1*((q**n)-1))/(q-1)

        resultado(f"A soma dos primeiros {n} termos da PG é:", calculo) if imprimir else None
        return calculo