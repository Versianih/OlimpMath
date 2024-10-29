from functions.functions import math, tratErro, resultado, ERROR


def raizQuadrada(a):
    if tratErro(float, [a]) == True:
        a = float(a)    
        calculo = (a)**(1/2)
        resultado("Raiz: " + str(calculo))
        return calculo

def Resto(a, b):
    if tratErro(float, [a, b]) == True:    
        a = float(a)
        b = float(b)
        calculo = math.remainder(a,b)
        resultado("Resto: " + str(calculo))
        return calculo
    

def MDC(a,b):
    if tratErro(int, [a, b]) == True:    
        a = int(a)
        b = int(b)
        calculo = math.gcd(a,b)
        resultado("MDC: " + str(calculo))
        return calculo
    

def MMC(a, b):
    if tratErro(int, [a, b]) == True:    
        a = int(a)
        b = int(b)
        calculo = (abs(a*b))/(math.gcd(a,b))
        resultado("MMC: " + str(calculo))
        return calculo
    

def equação2Grau(a,b,c):
    if tratErro(float, [a, b, c]) == True:
        a = float(a)
        b = float(b)
        c = float(c)
        if a != 0:    
            delta = b**2 - (4*a*c)
            if delta >= 0:
                x1 = (-b + (delta**(1/2)))/(2*a)
                x2 = (-b - (delta**(1/2)))/(2*a)
                resultado("As Raizes da Equação são: " + str(((x1), (x2))))
                return [x1, x2]
            else:
                cx1 = (-b + (delta**(1/2)))/(2*a)
                cx2 = (-b - (delta**(1/2)))/(2*a)
                resultado("As Raizes Complexas da Equação são: " + str(((cx1), (cx2))))
                return [cx1, cx2]
        else:
            return ERROR("'a' tem que ser diferente de 0")

# }