from functions.functions import math, pi, tratErro, resultado, ERROR, calcExpression


def distPontos(xa, ya, xb, yb, print=None):
    if tratErro(float, [xa, ya, xb, yb]) == True:
        xa = calcExpression(xa, float)
        ya = calcExpression(ya, float)
        xb = calcExpression(xb, float)
        yb = calcExpression(yb, float)
        calculo = (((xb - xa)**2) + ((yb - ya)**2))**(1/2)
        if calculo >= 0:    
            if print:
                resultado("A Distância entre os Pontos é:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Distância não pode ser negativa")
            return None