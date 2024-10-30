from functions.functions import math, pi, tratErro, resultado, ERROR


# Plana
def areaPoliRegular(qntLados, lado, print=None):
    if tratErro(int, [qntLados]) & tratErro(float, [lado]) == True:    
        qntLados = int(qntLados)
        lado = float(lado)
        if qntLados < 3:
            if print == True:
                ERROR("Verifique se a quantidade de lados permite um Polígono")
            return None
        elif qntLados == 3:
            Tricalculo = ((1 *((lado**2)*math.sqrt(3))) / 4)
            if Tricalculo >= 0:
                if print == True:
                    resultado("Área:", Tricalculo, True)
                return Tricalculo
            else:
                if print == True:
                    ERROR("Área não pode ser negativa")
                return None
        elif qntLados == 4:
            Quacalculo = lado**2
            if Quacalculo >= 0:
                if print == True:
                    resultado("Área:", Quacalculo, True)
                return Quacalculo
            else:
                if print == True:
                    ERROR("Área não pode ser negativa")
                return None
        else:
            calculo = ((qntLados * ((lado**2)*math.sqrt(3))) / 4)
            if calculo >= 0:    
                if print == True:
                    resultado("Área:", calculo, True)        
                return calculo
            else:
                if print == True:
                    ERROR("Área não pode ser negativa")
                return None


def areaCírculo(raio, print=None):
    if tratErro(float, [raio]) == True:
        raio = float(raio)
        calculo = (raio*raio)* pi
        if calculo >= 0:
            if print == True:
                resultado("Área:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Área não pode ser negativa")
            return None


def areaQuadrado(lado, print=None):
    if tratErro(float, [lado]) == True:
        lado = float(lado)
        calculo = (lado*lado)
        if calculo >= 0:
            if print == True:
                resultado("Área:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Área não pode ser negativa")
            return None


def areaTriangulo(base, altura, print=None):
    if tratErro(float, [base, altura]) == True:    
        base = float(base)
        altura = float(altura)
        calculo = (base*altura)/2   
        if calculo >= 0:    
            if print == True:
                resultado("Área:", calculo, True)
            return calculo
        else:    
            if print == True:
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
            if print == True:
                resultado("Área:", calculo, True) 
            return calculo
        else:
            if print == True:
                ERROR("Área não pode ser negativa")
            return None 


def areaTrapezio(BASE, base, altura, print=None):
    if tratErro(float, [BASE, base, altura]) == True:    
        BASE = float(BASE)
        base = float(base)
        altura = float(altura)
        calculo = ((BASE+base)*altura)/2
        if calculo >= 0:
            if print == True:
                resultado("Área:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Área não pode ser negativa")
            return None


def pitagorasHipotenusa(a,b, print=None):
    if tratErro(float, [a,b]) == True:
        a = float(a)
        b = float(b)
        calculo = ((a**2) + (b**2))**(1/2)
        if print == True:
            resultado("A medida da Hipotenusa é:", calculo, True)
        return calculo


def pitagorasCateto(a,h, print=None):
    if tratErro(float, [a,h]) == True:
        a = float(a)
        h = float(h)
        calculo = ((h**2) - (a**2))**(1/2)
        if print == True:
            resultado("A medida do Cateto é:", calculo, True)
        return calculo


# Espacial
def volumePrisma(qntlados, lado, altura, print=None):
    if tratErro(int, qntlados) & tratErro(float, [lado, altura]) == True:
        qntlados = int(qntlados)
        lado = float(lado)        
        altura = float(altura)
        if qntlados < 3:
            if print == True:
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
            if print == True:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Volume não pode ser negativo")
            return None


def volumeCubo(lado, print=None):
    if tratErro(float, [lado]) == True:
        lado = float(lado)
        calculo = lado**3
        if calculo >= 0:
            if print == True:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Volume não pode ser negativo")
            return None


def volumeParalelepipedo(a, b, h, print=None):
    if tratErro(float, [a, b, h]) == True:
        a = float(a)
        b = float(b)
        h = float(h)
        calculo = (a*b*h)
        if calculo >= 0:
            if print == True:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Volume não pode ser negativo")
            return None


def volumeCilindro(raio, h, print=None):
    if tratErro(float, [raio, h]) == True:    
        raio = float(raio)
        h = float(h)
        calculo = (pi*(raio**2))*h
        if calculo >= 0:
            if print == True:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Volume não pode ser negativo")
            return None


def volumeEsfera(raio, print=None):
    if tratErro(float, [raio]) == True:
        raio = float(raio)    
        calculo = (4/3)*pi*raio
        if calculo >= 0:    
            if print == True:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Volume não pode ser negativo")
            return None


def volumeCone(raio, h, print=None):
    if tratErro(float, [raio, h]) == True:
        raio = float(raio)
        h = float(h)
        calculo = (pi*(raio**2)*h)/3
        if calculo >= 0:
            if print == True:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Volume não pode ser negativo")
            return None


def volumeTroncoCone(R, r, h, print=None):
    if tratErro(float, [R, r, h]) == True:
        R = float(R)
        r = float(r)
        h = float(h)
        calculo = (pi*h*((R**2)+(r**2)+(R*r)))/3
        if calculo >= 0:    
            if print == True:
                resultado("Volume:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Volume não pode ser negativo")
            return None
        

# Analítica
def distPontos(xa, ya, xb, yb, print=None):
    if tratErro(float, [xa, ya, xb, yb]) == True:
        xa = float(xa)
        ya = float(ya)
        xb = float(xb)
        yb = float(yb)
        calculo = (((xb - xa)**2) + ((yb - ya)**2))**(1/2)
        if calculo >= 0:    
            if print == True:
                resultado("A Distância entre os Pontos é:", calculo, True)
            return calculo
        else:
            if print == True:
                ERROR("Distância não pode ser negativa")
            return None