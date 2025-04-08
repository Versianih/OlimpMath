from functions.tools import Tools, math
import functions.tools

def hipotenusa_com_oposto(a,b, imprimir=False):
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        
        if functions.tools.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.sin(b))

        Tools.resultado("Hipotenusa:", hipotenusa, aproximar=True) if imprimir else None
        return hipotenusa


def hipotenusa_com_adjacente(a,b, imprimir=False):
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        
        if functions.tools.entrada_angulo == "graus":
            b = math.radians(b)
        hipotenusa = a/(math.cos(b))

        Tools.resultado("Hipotenusa:", hipotenusa, aproximar=True) if imprimir else None
        return hipotenusa



def oposto_com_hipotenusa(a,b, imprimir=False):
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        
        if functions.tools.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.sin(b))
        
        Tools.resultado("Cateto Oposto:", oposto, aproximar=True) if imprimir else None
        return oposto


def oposto_com_adjacente(a,b, imprimir=False):
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)

        if functions.tools.entrada_angulo == "graus":
            b = math.radians(b)
        oposto = a*(math.tan(b))

        Tools.resultado("Cateto Oposto:", oposto, aproximar=True) if imprimir else None
        return oposto



def adjacente_com_hipotenusa(a,b, imprimir=False):
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        
        if functions.tools.entrada_angulo == "graus":        
            b = math.radians(b)
        adjacente = a*(math.cos(b))
        
        Tools.resultado("Cateto Adjacente:", adjacente, aproximar=True) if imprimir else None
        return adjacente


def adjacente_com_oposto(a,b, imprimir=False):
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        
        if functions.tools.entrada_angulo == "graus":
            b = math.radians(b)
        adjacente = a/(math.tan(b))
        
        Tools.resultado("Cateto Adjacente:", adjacente, aproximar=True) if imprimir else None
        return adjacente



def angulo_com_coca(a,b, imprimir=False): #a=CO b=CA
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        angulo = math.atan(a/b)
        
        if functions.tools.saida_angulo == "graus":
            angulo = math.degrees(angulo)

        Tools.resultado("Ângulo em " + str(functions.tools.saida_angulo) + ":", angulo, aproximar=True) if imprimir else None
        return angulo


def angulo_com_coh(a,b, imprimir=False): #a=CO b=H
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        angulo = math.asin(a/b)
        
        if functions.tools.saida_angulo == "graus":
            angulo = math.degrees(angulo)
        
        Tools.resultado("Ângulo em " + str(functions.tools.saida_angulo) + ":", angulo, aproximar=True) if imprimir else None
        return angulo


def angulo_com_cah(a,b, imprimir=False): #a=CA b=H
    if Tools.trat_erro(float, [a, b]):
        a = Tools.calc_expression(a, float)
        b = Tools.calc_expression(b, float)
        angulo = math.acos(a/b)
        
        if functions.tools.saida_angulo == "graus":
            angulo = math.degrees(angulo)

        Tools.resultado("Ângulo em " + str(functions.tools.saida_angulo) + ":", angulo, aproximar=True) if imprimir else None
        return angulo