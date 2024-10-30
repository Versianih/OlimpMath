from functions.functions import math, tratErro, resultado, ERROR
import functions.functions

def HipotenusaComOposto(a,b, print=None):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.sin(b))
        
        if print == True:
            resultado("Hipotenusa:", hipotenusa, True)
        return hipotenusa


def HipotenusaComAdjacente(a,b, print=None):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.cos(b))
        
        if print == True:
            resultado("Hipotenusa:", hipotenusa, True)
        return hipotenusa



def OpostoComHipotenusa(a,b, print=None):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.sin(b))
        
        if print == True:
            resultado("Cateto Oposto:", oposto, True)
        return oposto


def OpostoComAdjacente(a,b, print=None):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)

        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.tan(b))
        
        if print == True:
            resultado("Cateto Oposto:", oposto, True)
        return oposto



def AdjacenteComHipotenusa(a,b, print=None):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        
        if functions.functions.entrada_angulo == "graus":        
            b = math.radians(b)
        adjacente = a*(math.cos(b))
        
        if print == True:
            resultado("Cateto Adjacente:", adjacente, True)
        return adjacente


def AdjacenteComOposto(a,b, print=None):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        adjacente = a/(math.tan(b))
        
        if print == True:
            resultado("Cateto Adjacente:", adjacente, True)
        return adjacente



def AnguloComCOCA(a,b, print=None): #a=CO b=CA
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        angulo = math.atan(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)

        if print == True:
            resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, True)
        return angulo


def AnguloComCOH(a,b, print=None): #a=CO b=H
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        angulo = math.asin(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)
        
        if print == True:
            resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, True) 
        return angulo


def AnguloComCAH(a,b, print=None): #a=CA b=H
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        angulo = math.acos(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)
        
        if print == True:
            resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, True)
        return angulo