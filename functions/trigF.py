from functions.tools import Tools, math
import functions.tools

class Trigonometria:

    class Hipotenusa:

        @staticmethod
        def com_oposto(a, b, ENTRADA_ANGULO, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b]):
                return None

            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            
            if ENTRADA_ANGULO == "graus":
                b = math.radians(b)
            hipotenusa = a/(math.sin(b))

            Tools.resultado("Hipotenusa:", hipotenusa, aproximar=True) if imprimir else None
            return hipotenusa

        @staticmethod
        def com_adjacente(a, b, ENTRADA_ANGULO, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            
            if ENTRADA_ANGULO == "graus":
                b = math.radians(b)
            hipotenusa = a/(math.cos(b))

            Tools.resultado("Hipotenusa:", hipotenusa, aproximar=True) if imprimir else None
            return hipotenusa


    class Oposto:

        @staticmethod
        def com_hipotenusa(a, b, ENTRADA_ANGULO, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            
            if ENTRADA_ANGULO == "graus":
                b = math.radians(b)
            oposto = a*(math.sin(b))
            
            Tools.resultado("Cateto Oposto:", oposto, aproximar=True) if imprimir else None
            return oposto

        @staticmethod
        def com_adjacente(a, b, ENTRADA_ANGULO, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b]):
                return None
                
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)

            if ENTRADA_ANGULO == "graus":
                b = math.radians(b)
            oposto = a*(math.tan(b))

            Tools.resultado("Cateto Oposto:", oposto, aproximar=True) if imprimir else None
            return oposto


    class Adjacente:

        @staticmethod
        def com_hipotenusa(a, b, ENTRADA_ANGULO, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            
            if ENTRADA_ANGULO == "graus":        
                b = math.radians(b)
            adjacente = a*(math.cos(b))
            
            Tools.resultado("Cateto Adjacente:", adjacente, aproximar=True) if imprimir else None
            return adjacente

        @staticmethod
        def com_oposto(a, b, ENTRADA_ANGULO, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            
            if ENTRADA_ANGULO == "graus":
                b = math.radians(b)
            adjacente = a/(math.tan(b))
            
            Tools.resultado("Cateto Adjacente:", adjacente, aproximar=True) if imprimir else None
            return adjacente


    class Angulo:

        @staticmethod
        def com_coca(a, b, SAIDA_ANGULO, imprimir=False) -> float: #a=CO b=CA
            if not Tools.trat_erro(float, [a, b]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            angulo = math.atan(a/b)
            
            if SAIDA_ANGULO == "graus":
                angulo = math.degrees(angulo)

            Tools.resultado("Ângulo em " + str(SAIDA_ANGULO) + ":", angulo, aproximar=True) if imprimir else None
            return angulo

        @staticmethod
        def com_coh(a, b, SAIDA_ANGULO, imprimir=False) -> float: #a=CO b=H
            if not Tools.trat_erro(float, [a, b]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            angulo = math.asin(a/b)
            
            if SAIDA_ANGULO == "graus":
                angulo = math.degrees(angulo)
            
            Tools.resultado("Ângulo em " + str(SAIDA_ANGULO) + ":", angulo, aproximar=True) if imprimir else None
            return angulo

        @staticmethod
        def com_cah(a, b, SAIDA_ANGULO, imprimir=False) -> float: #a=CA b=H
            if not Tools.trat_erro(float, [a, b]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            angulo = math.acos(a/b)
            
            if SAIDA_ANGULO == "graus":
                angulo = math.degrees(angulo)

            Tools.resultado("Ângulo em " + str(SAIDA_ANGULO) + ":", angulo, aproximar=True) if imprimir else None
            return angulo