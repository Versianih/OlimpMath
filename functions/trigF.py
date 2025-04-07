from functions.functions import math, trat_erro, resultado, calc_expression
import functions.functions

def hipotenusa_com_oposto(a,b, imprimir=False):
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.sin(b))

        resultado("Hipotenusa:", hipotenusa, aproximar=True) if imprimir else None
        return hipotenusa


def hipotenusa_com_adjacente(a,b, imprimir=False):
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.cos(b))

        resultado("Hipotenusa:", hipotenusa, aproximar=True) if imprimir else None
        return hipotenusa



def oposto_com_hipotenusa(a,b, imprimir=False):
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.sin(b))
        
        resultado("Cateto Oposto:", oposto, aproximar=True) if imprimir else None
        return oposto


def oposto_com_adjacente(a,b, imprimir=False):
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)

        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.tan(b))

        resultado("Cateto Oposto:", oposto, aproximar=True) if imprimir else None
        return oposto



def adjacente_com_hipotenusa(a,b, imprimir=False):
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        
        if functions.functions.entrada_angulo == "graus":        
            b = math.radians(b)
        adjacente = a*(math.cos(b))
        
        resultado("Cateto Adjacente:", adjacente, aproximar=True) if imprimir else None
        return adjacente


def adjacente_com_oposto(a,b, imprimir=False):
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        
        if functions.functions.entrada_angulo == "graus":
            b = math.radians(b)
        adjacente = a/(math.tan(b))
        
        resultado("Cateto Adjacente:", adjacente, aproximar=True) if imprimir else None
        return adjacente



def angulo_com_coca(a,b, imprimir=False): #a=CO b=CA
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        angulo = math.atan(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)

        resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, aproximar=True) if imprimir else None
        return angulo


def angulo_com_coh(a,b, imprimir=False): #a=CO b=H
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        angulo = math.asin(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)
        
        resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, aproximar=True) if imprimir else None
        return angulo


def angulo_com_cah(a,b, imprimir=False): #a=CA b=H
    if trat_erro(float, [a, b]):
        a = calc_expression(a, float)
        b = calc_expression(b, float)
        angulo = math.acos(a/b)
        
        if functions.functions.saida_angulo == "graus":
            angulo = math.degrees(angulo)

        resultado("Ângulo em " + str(functions.functions.saida_angulo) + ":", angulo, aproximar=True) if imprimir else None
        return angulo