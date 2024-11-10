from functions.functions import math, pi, tratErro, resultado, ERROR, calcExpression


def volumePrisma(qntlados, lado, altura, print=None):
    if tratErro(int, qntlados) and tratErro(float, [lado, altura]) == True:
        qntlados = calcExpression(qntlados, int)
        lado = calcExpression(lado, float)
        altura = calcExpression(altura, float)
        if qntlados < 3:
            if print:
                ERROR("Verifique se a quantidade de lados permite a base")
            return None
        elif qntlados == 3:
            base = ((1 *((lado**2)*math.sqrt(3))) / 4)
        elif qntlados == 4:
            base = lado**2
        else:
            base = ((qntlados * ((lado**2)*math.sqrt(3))) / 4)
        calculo = base*altura
        if calculo >= 0:
            if print:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Volume não pode ser negativo")
            return None


def volumeCubo(lado, print=None):
    if tratErro(float, [lado]) == True:
        lado = calcExpression(lado, float)
        calculo = lado**3
        if calculo >= 0:
            if print:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Volume não pode ser negativo")
            return None


def volumeParalelepipedo(a, b, h, print=None):
    if tratErro(float, [a, b, h]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        h = calcExpression(h, float)
        calculo = (a*b*h)
        if calculo >= 0:
            if print:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Volume não pode ser negativo")
            return None


def volumeCilindro(raio, h, print=None):
    if tratErro(float, [raio, h]) == True:    
        raio = calcExpression(raio, float)
        h = calcExpression(h, float)
        calculo = (pi*(raio**2))*h
        if calculo >= 0:
            if print:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Volume não pode ser negativo")
            return None


def volumeEsfera(raio, print=None):
    if tratErro(float, [raio]) == True:
        raio = calcExpression(raio, float)
        calculo = (4/3)*pi*raio
        if calculo >= 0:    
            if print:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Volume não pode ser negativo")
            return None


def volumeCone(raio, h, print=None):
    if tratErro(float, [raio, h]) == True:
        raio = calcExpression(raio, float)
        h = calcExpression(h, float)
        calculo = (pi*(raio**2)*h)/3
        if calculo >= 0:
            if print:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Volume não pode ser negativo")
            return None


def volumeTroncoCone(R, r, h, print=None):
    if tratErro(float, [R, r, h]) == True:
        R = calcExpression(R, float)
        r = calcExpression(r, float)
        h = calcExpression(h, float)
        calculo = (pi*h*((R**2)+(r**2)+(R*r)))/3
        if calculo >= 0:    
            if print:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Volume não pode ser negativo")
            return None