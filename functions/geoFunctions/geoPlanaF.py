import os
from functions.tools import Tools, math
from sympy import nsimplify, simplify, pi

class Geometria_Plana:

    class Area:

        @staticmethod       
        def area_poligono_regular(qntLados, lado, imprimir=False) -> float:
            if not (Tools.trat_erro(int, [qntLados]) and Tools.trat_erro(float, [lado])):
                return None
                
            qntLados = Tools.calc_expression(qntLados, int)
            lado = Tools.calc_expression(lado, float)
            
            if qntLados < 3:
                Tools.ERROR("Verifique se a quantidade de lados permite um Polígono") if imprimir else None
                return None
                
            if qntLados == 3:
                area = ((lado**2) * math.sqrt(3)) / 4
            elif qntLados == 4:
                area = lado**2
            else:
                area = (qntLados * (lado**2) * math.sqrt(3)) / 4
                
            if area < 0:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return None
                
            Tools.resultado("Área:", area, aproximar=True) if imprimir else None
            return area

        @staticmethod
        def area_circulo(raio, imprimir=False) -> float:
            if not Tools.trat_erro(float, [raio]): 
                return None

            raio = Tools.calc_expression(raio, float)
            if raio < 0:
                Tools.ERROR("O raio não pode ser negativo") if imprimir else None
                return None
            
            if os.getenv("SAIDA_PI") == 'True':
                raio = nsimplify(raio)
                area = pi * raio**2
                area = simplify(area)
                area = str(area).replace('*pi', 'π').replace('pi', 'π')
            else:
                area = raio**2 * math.pi
                
            Tools.resultado("Área:", area, aproximar=True if os.getenv("SAIDA_PI") == 'False' else False) if imprimir else None
            return area

        @staticmethod
        def area_quadrado(lado, imprimir=False) -> float:
            if not Tools.trat_erro(float, [lado]):
                return None
                
            lado = Tools.calc_expression(lado, float)
            area = lado**2
            
            if area < 0:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return None
                
            Tools.resultado("Área:", area, aproximar=True) if imprimir else None
            return area

        @staticmethod
        def area_triangulo(base, altura, imprimir=False) -> float:
            if not Tools.trat_erro(float, [base, altura]):
                return None
                
            base = Tools.calc_expression(base, float)
            altura = Tools.calc_expression(altura, float)
            area = (base * altura) / 2
            
            if area < 0:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return None
                
            Tools.resultado("Área:", area, aproximar=True) if imprimir else None
            return area

        @staticmethod
        def area_triangulo_heron(a, b, c, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b, c]):
                return None
                
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            c = Tools.calc_expression(c, float)
            
            p = (a + b + c) / 2
            area = math.sqrt(p * (p-a) * (p-b) * (p-c))
            
            if area < 0:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return None

            Tools.resultado("Área:", area, aproximar=True) if imprimir else None
            return area

        @staticmethod
        def area_trapezio(BASE, base, altura, imprimir=False) -> float:
            if not Tools.trat_erro(float, [BASE, base, altura]):
                return None
                
            BASE = Tools.calc_expression(BASE, float)
            base = Tools.calc_expression(base, float)
            altura = Tools.calc_expression(altura, float)
            
            area = ((BASE + base) * altura) / 2
            
            if area < 0:
                Tools.ERROR("Área não pode ser negativa") if imprimir else None
                return None

            Tools.resultado("Área:", area, aproximar=True) if imprimir else None
            return area


    class Pitagoras:

        @staticmethod
        def pitagoras_hipotenusa(a, b, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b]):
                return None
                
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            
            hipotenusa = math.sqrt(a**2 + b**2)
            
            Tools.resultado("A medida da Hipotenusa é:", hipotenusa, aproximar=True) if imprimir else None
            return hipotenusa

        @staticmethod
        def pitagoras_cateto(a, h, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, h]):
                return None
                
            a = Tools.calc_expression(a, float)
            h = Tools.calc_expression(h, float)
            
            # Verificar se a hipotenusa é maior que o cateto conhecido
            if h <= a:
                Tools.ERROR("A hipotenusa deve ser maior que o cateto") if imprimir else None
                return None
                
            cateto = math.sqrt(h**2 - a**2)
            
            Tools.resultado("A medida do Cateto é:", cateto, aproximar=True) if imprimir else None
            return cateto


    class Poligonos:

        @staticmethod
        def formacao_triangulo(a, b, c, imprimir=False) -> bool:
            if not Tools.trat_erro(float, [a, b, c]):
                return None
                
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            c = Tools.calc_expression(c, float)
            
            forma_triangulo = (a + b > c) and (a + c > b) and (b + c > a)
            
            if imprimir:
                msg = f"Os valores {a}, {b}, {c} {'formam' if forma_triangulo else 'NÃO formam'} um triângulo"
                Tools.resultado(msg)
                
            return forma_triangulo