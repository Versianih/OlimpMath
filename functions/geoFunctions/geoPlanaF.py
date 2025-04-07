from functions.functions import math, pi, trat_erro, resultado, ERROR, calc_expression


def area_poligono_regular(qntLados, lado, imprimir=False):
    if trat_erro(int, [qntLados]) and trat_erro(float, [lado]):    
        qntLados = calc_expression(qntLados, int)
        lado = calc_expression(lado, float)
        if qntLados < 3:
            ERROR("Verifique se a quantidade de lados permite um Polígono") if imprimir else None
            return
        elif qntLados == 3:
            Tricalculo = ((1 *((lado**2)*math.sqrt(3))) / 4)
            if Tricalculo >= 0:
                resultado("Área:", Tricalculo, aproximar=True) if imprimir else None
                return Tricalculo
            else:
                ERROR("Área não pode ser negativa") if imprimir else None
                return
        elif qntLados == 4:
            Quacalculo = lado**2
            if Quacalculo >= 0:
                if imprimir:
                    resultado("Área:", Quacalculo, aproximar=True)
                return Quacalculo
            else:
                ERROR("Área não pode ser negativa") if imprimir else None
                return
        else:
            calculo = ((qntLados * ((lado**2)*math.sqrt(3))) / 4)
            if calculo >= 0:
                resultado("Área:", calculo, aproximar=True) if imprimir else None
                return calculo
            else:
                ERROR("Área não pode ser negativa") if imprimir else None
                return


def area_circulo(raio, imprimir=False):
    if trat_erro(float, [raio]):
        raio = calc_expression(raio, float)
        calculo = (raio*raio)* pi
        if calculo >= 0:
            resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_quadrado(lado, imprimir=False):
    if trat_erro(float, [lado]):
        lado = calc_expression(lado, float)
        calculo = (lado*lado)
        if calculo >= 0:
            resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_triangulo(base, altura, imprimir=False):
    if trat_erro(float, [base, altura]):
        base = calc_expression(base, float)
        altura = calc_expression(altura, float)
        calculo = (base*altura)/2   
        if calculo >= 0:
            resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:    
            ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_triangulo_heron(a, b, c, imprimir=False):
    if trat_erro(float, [a, b, c]):    
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        c = calc_expression(c, float)
        p = (a + b + c)/2
        calculo = math.sqrt(p*(p-a)*(p-b)*(p-c))
        if calculo >= 0:
            resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_trapezio(BASE, base, altura, imprimir=False):
    if trat_erro(float, [BASE, base, altura]):    
        BASE = calc_expression(BASE, float)
        base = calc_expression(base, float)
        altura = calc_expression(altura, float)
        calculo = ((BASE+base)*altura)/2
        if calculo >= 0:
            resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            ERROR("Área não pode ser negativa") if imprimir else None
            return


def pitagoras_hipotenusa(a,b, imprimir=False):
    if trat_erro(float, [a,b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        calculo = ((a**2) + (b**2))**(1/2)
        
        resultado("A medida da Hipotenusa é:", calculo, aproximar=True) if imprimir else None
        return calculo


def pitagoras_cateto(a,h, imprimir=False):
    if trat_erro(float, [a,h]):
        a = calc_expression(a, float)
        h = calc_expression(h, float)
        calculo = ((h**2) - (a**2))**(1/2)

        resultado("A medida do Cateto é:", calculo, aproximar=True) if imprimir else None
        return calculo
    

def formacao_triangulo(a, b, c, imprimir=False):
    if trat_erro(float, [a, b, c]):
        a = calc_expression(a, int)
        b = calc_expression(b, int)
        c = calc_expression(c, int)
        if a + b > c and a + c > b and b + c > a:
            resultado(f"Os valores {a}, {b}, {c} formam um triângulo") if imprimir else None
        else:
            resultado(f"Os valores {a}, {b}, {c} NÃO formam um triângulo") if imprimir else None