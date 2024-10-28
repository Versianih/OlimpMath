from functions.functions import math, pi, tratErro, resultado, ERROR


# Plana
def areaPoliRegular(qntLados, lado):
    if tratErro(int, [qntLados]) & tratErro(float, [lado]) == True:    
        qntLados = int(qntLados)
        lado = float(lado)
        if qntLados < 3:
            return ERROR("Verifique se a quantidade de lados permite um Polígono")
        elif qntLados == 3:
            Tricalculo = ((1 *((lado**2)*math.sqrt(3))) / 4)
            if Tricalculo >= 0:
                return resultado("Área: " + str(Tricalculo))
            else:
                return ERROR("Área não pode ser negativa")
        elif qntLados == 4:
            Quacalculo = lado**2
            if Quacalculo >= 0:
                return resultado("Área: " + str(Quacalculo))
            else:
                return ERROR("Área não pode ser negativa")
        else:
            calculo = ((qntLados * ((lado**2)*math.sqrt(3))) / 4)
            if calculo >= 0:    
                return resultado("Área: " + str(calculo))        
            else:
                return ERROR("Área não pode ser negativa")


def areaCírculo(raio):
    if tratErro(float, [raio]) == True:
        raio = float(raio)
        calculo = (raio*raio)* pi
        if calculo >= 0:
            return resultado("Área: " + str(calculo))
        else:
            return ERROR("Área não pode ser negativa")


def areaQuadrado(lado):
    if tratErro(float, [lado]) == True:
        lado = float(lado)
        calculo = (lado*lado)
        if calculo >= 0:
            return resultado("Área: " + str(calculo))
        else:
            return ERROR("Área não pode ser negativa")


def areaTriangulo(base, altura):
    if tratErro(float, [base, altura]) == True:    
        base = float(base)
        altura = float(altura)
        calculo = (base*altura)/2   
        if calculo >= 0:    
            return resultado("Área: " + str(calculo))
        else:    
            return ERROR("Área não pode ser negativa")


def areaTrianguloHeron(a, b, c):
    if tratErro(float, [a, b, c]) == True:    
        a = float(a)
        b = float(b)
        c = float(c)
        p = (a + b + c)/2
        calculo = math.sqrt(p*(p-a)*(p-b)*(p-c))
        if calculo >= 0:
            return resultado("Área: " + str(calculo)) 
        else:
            return ERROR("Área não pode ser negativa")


def areaTrapezio(BASE, base, altura):
    if tratErro(float, [BASE, base, altura]) == True:    
        BASE = float(BASE)
        base = float(base)
        altura = float(altura)
        calculo = ((BASE+base)*altura)/2
        if calculo >= 0:
            return resultado("Área: " + str(calculo))
        else:
            return ERROR("Área não pode ser negativa")


# Espacial
def volumePrisma(qntlados, lado, altura):
    if tratErro(int, qntlados) & tratErro(float, [lado, altura]) == True:
        qntlados = int(qntlados)
        lado = float(lado)        
        altura = float(altura)
        if qntlados < 3:
            return ERROR("Verifique se a quantidade de lados permite a base")
        elif qntlados == 3:
            base = ((1 *((lado**2)*math.sqrt(3))) / 4)
        elif qntlados == 4:
            base = lado**2
        else:
            base = ((qntlados * ((lado**2)*math.sqrt(3))) / 4)
        calculo = base*altura
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")


def volumeCubo(lado):
    if tratErro(float, [lado]) == True:
        lado = float(lado)
        calculo = lado**3
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")


def volumeParalelepipedo(a,b,h):
    if tratErro(float, [a, b, h]) == True:
        a = float(a)
        b = float(b)
        h = float(h)
        calculo = (a*b*h)
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")


def volumeCilindro(raio, h):
    if tratErro(float, [raio, h]) == True:    
        raio = float(raio)
        h = float(h)
        calculo = (pi*(raio**2))*h
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")


def volumeEsfera(raio):
    if tratErro(float, [raio]) == True:
        raio = float(raio)    
        calculo = (4/3)*pi*raio
        if calculo >= 0:    
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")


def volumeCone(raio, h):
    if tratErro(float, [raio, h]) == True:
        raio = float(raio)
        h = float(h)
        calculo = (pi*(raio**2)*h)/3
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")


def volumeTroncoCone(R, r, h):
    if tratErro(float, [R, r, h]) == True:
        R = float(R)
        r = float(r)
        h = float(h)
        calculo = (pi*h*((R**2)+(r**2)+(R*r)))/3
        if calculo >= 0:    
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")
        

# Analítica
def distPontos(xa, ya, xb, yb):
    if tratErro(float, [xa, ya, xb, yb]) == True:
        xa = float(xa)
        ya = float(ya)
        xb = float(xb)
        yb = float(yb)
        calculo = (((xb - xa)**2) + ((yb - ya)**2))**(1/2)
        if calculo >= 0:    
            return resultado("A Distância entre os Pontos é: " + str(calculo))
        else:
            return ERROR("Distância não pode ser negativa")