from functions.functions import math, tratErro, resultado, ERROR


def HipotenusaComOposto(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)    
        ang = math.radians(b)
        hipotenusa = a/(math.sin(ang))
        return resultado("Hipotenusa: " + str(hipotenusa))


def HipotenusaComAdjacente(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        hipotenusa = a/(math.cos(ang))
        return resultado("Hipotenusa: " + str(hipotenusa))



def OpostoComHipotenusa(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        oposto = a*(math.sin(ang))
        return resultado("Cateto Oposto: " + str(oposto))


def OpostoComAdjacente(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        oposto = a*(math.tan(ang))
        return resultado("Cateto Oposto: " + str(oposto))



def AdjacenteComHipotenusa(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        adjacente = a*(math.cos(ang))
        return resultado("Cateto Adjacente: " + str(adjacente))


def AdjacenteComOposto(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        adjacente = a/(math.tan(ang))
        return resultado("Cateto Adjacente: " + str(adjacente))



def AnguloComCOCA(a,b): #a=CO b=CA
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang_rad = math.atan(a/b)
        angulo = math.degrees(ang_rad)
        return resultado("Ângulo: " + str(angulo))


def AnguloComCOH(a,b): #a=CO b=H
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang_rad = math.asin(a/b)
        angulo = math.degrees(ang_rad)
        return resultado("Ângulo: " + str(angulo)) 


def AnguloComCAH(a,b): #a=CA b=H
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang_rad = math.acos(a/b)
        angulo = math.degrees(ang_rad)
        return resultado("Ângulo: " + str(angulo))