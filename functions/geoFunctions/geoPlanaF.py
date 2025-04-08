from functions.tools import Tools, math, pi


def area_poligono_regular(qntLados, lado, imprimir=False):
    if Tools.trat_erro(int, [qntLados]) and Tools.trat_erro(float, [lado]):    
        qntLados = Tools.calc_expression(qntLados, int)
        lado = Tools.calc_expression(lado, float)
        if qntLados < 3:
            Tools.ERROR("Verifique se a quantidade de lados permite um Polígono") if imprimir else None
            return
        elif qntLados == 3:
            Tricalculo = ((1 *((lado**2)*math.sqrt(3))) / 4)
            if Tricalculo >= 0:
                Tools.resultado("Área:", Tricalculo, aproximar=True) if imprimir else None
                return Tricalculo
            else:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return
        elif qntLados == 4:
            Quacalculo = lado**2
            if Quacalculo >= 0:
                if imprimir:
                    Tools.resultado("Área:", Quacalculo, aproximar=True)
                return Quacalculo
            else:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return
        else:
            calculo = ((qntLados * ((lado**2)*math.sqrt(3))) / 4)
            if calculo >= 0:
                Tools.resultado("Área:", calculo, aproximar=True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return


def area_circulo(raio, imprimir=False):
    if Tools.trat_erro(float, [raio]):
        raio = Tools.calc_expression(raio, float)
        calculo = (raio*raio)* pi
        if calculo >= 0:
            Tools.resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            Tools.ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_quadrado(lado, imprimir=False):
    if Tools.trat_erro(float, [lado]):
        lado = Tools.calc_expression(lado, float)
        calculo = (lado*lado)
        if calculo >= 0:
            Tools.resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            Tools.ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_triangulo(base, altura, imprimir=False):
    if Tools.trat_erro(float, [base, altura]):
        base = Tools.calc_expression(base, float)
        altura = Tools.calc_expression(altura, float)
        calculo = (base*altura)/2   
        if calculo >= 0:
            Tools.resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:    
            Tools.ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_triangulo_heron(a, b, c, imprimir=False):
    if Tools.trat_erro(float, [a, b, c]):    
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        c = Tools.calc_expression(c, float)
        p = (a + b + c)/2
        calculo = math.sqrt(p*(p-a)*(p-b)*(p-c))
        if calculo >= 0:
            Tools.resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            Tools.ERROR("Área não pode ser negativa") if imprimir else None
            return


def area_trapezio(BASE, base, altura, imprimir=False):
    if Tools.trat_erro(float, [BASE, base, altura]):    
        BASE = Tools.calc_expression(BASE, float)
        base = Tools.calc_expression(base, float)
        altura = Tools.calc_expression(altura, float)
        calculo = ((BASE+base)*altura)/2
        if calculo >= 0:
            Tools.resultado("Área:", calculo, aproximar=True) if imprimir else None
            return calculo
        else:
            Tools.ERROR("Área não pode ser negativa") if imprimir else None
            return


def pitagoras_hipotenusa(a,b, imprimir=False):
    if Tools.trat_erro(float, [a,b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        calculo = ((a**2) + (b**2))**(1/2)
        
        Tools.resultado("A medida da Hipotenusa é:", calculo, aproximar=True) if imprimir else None
        return calculo


def pitagoras_cateto(a,h, imprimir=False):
    if Tools.trat_erro(float, [a,h]):
        a = Tools.calc_expression(a, float)
        h = Tools.calc_expression(h, float)
        calculo = ((h**2) - (a**2))**(1/2)

        Tools.resultado("A medida do Cateto é:", calculo, aproximar=True) if imprimir else None
        return calculo
    

def formacao_triangulo(a, b, c, imprimir=False):
    if Tools.trat_erro(float, [a, b, c]):
        a = Tools.calc_expression(a, int)
        b = Tools.calc_expression(b, int)
        c = Tools.calc_expression(c, int)
        if a + b > c and a + c > b and b + c > a:
            Tools.resultado(f"Os valores {a}, {b}, {c} formam um triângulo") if imprimir else None
        else:
            Tools.resultado(f"Os valores {a}, {b}, {c} NÃO formam um triângulo") if imprimir else None