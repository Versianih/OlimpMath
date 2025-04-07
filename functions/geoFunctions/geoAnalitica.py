from functions.functions import trat_erro, resultado, ERROR, calc_expression


def distancia_entre_pontos(xa, ya, xb, yb, imprimir=False):
    if trat_erro(float, [xa, ya, xb, yb]):
        xa = calc_expression(xa, float)
        ya = calc_expression(ya, float)
        xb = calc_expression(xb, float)
        yb = calc_expression(yb, float)
        calculo = (((xb - xa)**2) + ((yb - ya)**2))**(1/2)
        if calculo >= 0:    
            resultado("A Distância entre os Pontos é:", calculo, True) if imprimir else None
            return calculo
        else:
            ERROR("Distância não pode ser negativa") if imprimir == True else None

def retangulos_em_uma_malha(n, m, imprimir=False): 
    if trat_erro(int, [n, m]):
        n = calc_expression(n, int)
        m = calc_expression(m, int)
        retangulos = (m * n * (n + 1) * (m + 1)) // 4
        resultado(f"A quantidade de retângulos possíveis em uma malha {n}x{m} é de: {retangulos} retângulos") if imprimir else None
        return retangulos 