from functions.functions import math, tratErro, resultado, ERROR, calcExpression
import functions.functions

def HipotenusaComOposto(a,b, imprimir=None):
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.sin(b))
        
        if imprimir == True:
            resultado("Hipotenusa:", hipotenusa, True)
        return hipotenusa


def HipotenusaComAdjacente(a,b, imprimir=None):
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.cos(b))
        
        if imprimir == True:
            resultado("Hipotenusa:", hipotenusa, True)
        return hipotenusa



def OpostoComHipotenusa(a,b, imprimir=None):
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.sin(b))
        
        if imprimir == True:
            resultado("Cateto Oposto:", oposto, True)
        return oposto


def OpostoComAdjacente(a,b, imprimir=None):
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)

        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.tan(b))
        
        if imprimir:
            resultado("Cateto Oposto:", oposto, True)
        return oposto



def AdjacenteComHipotenusa(a,b, imprimir=None):
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        
        if functions.functions.entrada_angulo == "graus":        
            b = math.radians(b)
        adjacente = a*(math.cos(b))
        
        if imprimir:
            resultado("Cateto Adjacente:", adjacente, True)
        return adjacente


def AdjacenteComOposto(a,b, imprimir=None):
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        adjacente = a/(math.tan(b))
        
        if imprimir:
            resultado("Cateto Adjacente:", adjacente, True)
        return adjacente



def AnguloComCOCA(a,b, imprimir=None): #a=CO b=CA
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        angulo = math.atan(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)

        if imprimir:
            resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, True)
        return angulo


def AnguloComCOH(a,b, imprimir=None): #a=CO b=H
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        angulo = math.asin(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)
        
        if imprimir:
            resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, True) 
        return angulo


def AnguloComCAH(a,b, imprimir=None): #a=CA b=H
    if tratErro(float, [a, b]) == True:
        a = calcExpression(a, float)
        b = calcExpression(b, float)
        angulo = math.acos(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)
        
        if imprimir:
            resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, True)
        return angulo