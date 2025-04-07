from functions.functions import math, pi, trat_erro, resultado, ERROR, calc_expression


def volume_prisma(qntlados, lado, altura, imprimir=False):
    if trat_erro(int, qntlados) and trat_erro(float, [lado, altura]):
        qntlados = calc_expression(qntlados, int)
        lado = calc_expression(lado, float)
        altura = calc_expression(altura, float)
        if qntlados < 3:
            ERROR("Verifique se a quantidade de lados permite a base") if imprimir else None
            return
        elif qntlados == 3:
            base = ((1 *((lado**2)*math.sqrt(3))) / 4)
        elif qntlados == 4:
            base = lado**2
        else:
            base = ((qntlados * ((lado**2)*math.sqrt(3))) / 4)
        calculo = base*altura
        if calculo >= 0:
            resultado("Volume:", calculo, True) if imprimir else None
            return calculo
        else:
            ERROR("Volume não pode ser negativo") if imprimir else None
            return


def volume_cubo(lado, imprimir=False):
    if trat_erro(float, [lado]):
        lado = calc_expression(lado, float)
        calculo = lado**3
        if calculo >= 0:
            resultado("Volume:", calculo, True) if imprimir else None
            return calculo
        else:
            ERROR("Volume não pode ser negativo") if imprimir else None
            return


def volume_paralelepipedo(a, b, h, imprimir=False):
    if trat_erro(float, [a, b, h]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        h = calc_expression(h, float)
        calculo = (a*b*h)
        if calculo >= 0:
            resultado("Volume:", calculo, True) if imprimir else None
            return calculo
        else:
            ERROR("Volume não pode ser negativo") if imprimir else None
            return


def volume_cilindro(raio, h, imprimir=False):
    if trat_erro(float, [raio, h]):    
        raio = calc_expression(raio, float)
        h = calc_expression(h, float)
        calculo = (pi*(raio**2))*h
        if calculo >= 0:
            resultado("Volume:", calculo, True) if imprimir else None
            return calculo
        else:
            ERROR("Volume não pode ser negativo") if imprimir else None
            return


def volume_esfera(raio, imprimir=False):
    if trat_erro(float, [raio]):
        raio = calc_expression(raio, float)
        calculo = (4/3)*pi*raio
        if calculo >= 0:    
            resultado("Volume:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            ERROR("Volume não pode ser negativo") if imprimir else None
            return


def volume_cone(raio, h, imprimir=False):
    if trat_erro(float, [raio, h]):
        raio = calc_expression(raio, float)
        h = calc_expression(h, float)
        calculo = (pi*(raio**2)*h)/3
        if calculo >= 0:
            resultado("Volume:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            ERROR("Volume não pode ser negativo") if imprimir else None
            return


def volume_tronco_cone(R, r, h, imprimir=False):
    if trat_erro(float, [R, r, h]):
        R = calc_expression(R, float)
        r = calc_expression(r, float)
        h = calc_expression(h, float)
        calculo = (pi*h*((R**2)+(r**2)+(R*r)))/3
        if calculo >= 0:    
            resultado("Volume:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            ERROR("Volume não pode ser negativo") if imprimir else None
            return