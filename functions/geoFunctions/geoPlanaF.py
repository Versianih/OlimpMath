from functions.functions import math, pi, tratErro, resultado, ERROR


def areaPoliRegular(qntLados, lado, print=None):
    if tratErro(int, [qntLados]) and tratErro(float, [lado]) == True:    
        qntLados = int(qntLados)
        lado = float(lado)
        if qntLados < 3:
            if print:
                ERROR("Verifique se a quantidade de lados permite um Polígono")
            return None
        elif qntLados == 3:
            Tricalculo = ((1 *((lado**2)*math.sqrt(3))) / 4)
            if Tricalculo >= 0:
                if print:
                    resultado("Área:", Tricalculo, True)
                return Tricalculo
            else:
                if print:
                    ERROR("Área não pode ser negativa")
                return None
        elif qntLados == 4:
            Quacalculo = lado**2
            if Quacalculo >= 0:
                if print:
                    resultado("Área:", Quacalculo, True)
                return Quacalculo
            else:
                if print:
                    ERROR("Área não pode ser negativa")
                return None
        else:
            calculo = ((qntLados * ((lado**2)*math.sqrt(3))) / 4)
            if calculo >= 0:    
                if print:
                    resultado("Área:", calculo, True)        
                return calculo
            else:
                if print:
                    ERROR("Área não pode ser negativa")
                return None


def areaCírculo(raio, print=None):
    if tratErro(float, [raio]) == True:
        raio = float(raio)
        calculo = (raio*raio)* pi
        if calculo >= 0:
            if print:
                resultado("Área:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Área não pode ser negativa")
            return None


def areaQuadrado(lado, print=None):
    if tratErro(float, [lado]) == True:
        lado = float(lado)
        calculo = (lado*lado)
        if calculo >= 0:
            if print:
                resultado("Área:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Área não pode ser negativa")
            return None


def areaTriangulo(base, altura, print=None):
    if tratErro(float, [base, altura]) == True:    
        base = float(base)
        altura = float(altura)
        calculo = (base*altura)/2   
        if calculo >= 0:    
            if print:
                resultado("Área:", calculo, True)
            return calculo
        else:    
            if print:
                ERROR("Área não pode ser negativa")
            return None


def areaTrianguloHeron(a, b, c, print=None):
    if tratErro(float, [a, b, c]) == True:    
        a = float(a)
        b = float(b)
        c = float(c)
        p = (a + b + c)/2
        calculo = math.sqrt(p*(p-a)*(p-b)*(p-c))
        if calculo >= 0:
            if print:
                resultado("Área:", calculo, True) 
            return calculo
        else:
            if print:
                ERROR("Área não pode ser negativa")
            return None 


def areaTrapezio(BASE, base, altura, print=None):
    if tratErro(float, [BASE, base, altura]) == True:    
        BASE = float(BASE)
        base = float(base)
        altura = float(altura)
        calculo = ((BASE+base)*altura)/2
        if calculo >= 0:
            if print:
                resultado("Área:", calculo, True)
            return calculo
        else:
            if print:
                ERROR("Área não pode ser negativa")
            return None


def pitagorasHipotenusa(a,b, print=None):
    if tratErro(float, [a,b]) == True:
        a = float(a)
        b = float(b)
        calculo = ((a**2) + (b**2))**(1/2)
        if print:
            resultado("A medida da Hipotenusa é:", calculo, True)
        return calculo


def pitagorasCateto(a,h, print=None):
    if tratErro(float, [a,h]) == True:
        a = float(a)
        h = float(h)
        calculo = ((h**2) - (a**2))**(1/2)
        if print:
            resultado("A medida do Cateto é:", calculo, True)
        return calculo
    

def formaçãoTriângulo(a, b, c, print=None):
    if tratErro(float, [a, b, c]):
        a = int(a)
        b = int(b)
        c = int(c)
        if a + b > c and a + c > b and b + c > a:
            if print:
                resultado(f"Os valores {a}, {b}, {c} formam um triângulo")
        else:
            resultado(f"Os valores {a}, {b}, {c} NÃO formam um triângulo")