import os
from functions.tools import Tools, math
from sympy import simplify, nsimplify, pi

class Geometria_Espacial:

    class Volume:

        @staticmethod
        def volume_prisma(qntlados, lado, altura, imprimir=False) -> float:
            if not Tools.trat_erro(int, qntlados) and Tools.trat_erro(float, [lado, altura]):
                return None
            
            qntlados = Tools.calc_expression(qntlados, int)
            lado = Tools.calc_expression(lado, float)
            altura = Tools.calc_expression(altura, float)
            
            if qntlados < 3:
                Tools.ERROR("Verifique se a quantidade de lados permite a base") if imprimir else None
                return
            elif qntlados == 3:
                base = ((1 * ((lado**2) * math.sqrt(3))) / 4)
            elif qntlados == 4:
                base = lado**2
            else:
                base = ((qntlados * ((lado**2) * math.sqrt(3))) / 4)
            
            calculo = base * altura
            if calculo >= 0:
                Tools.resultado("Volume:", calculo, True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

        @staticmethod
        def volume_cubo(lado, imprimir=False) -> float:
            if not Tools.trat_erro(float, [lado]):
                return None
            
            lado = Tools.calc_expression(lado, float)
            
            calculo = lado**3
            if calculo >= 0:
                Tools.resultado("Volume:", calculo, True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

        @staticmethod
        def volume_paralelepipedo(a, b, h, imprimir=False) -> float:
            if not Tools.trat_erro(float, [a, b, h]):
                return None
            
            a = Tools.calc_expression(a, float)
            b = Tools.calc_expression(b, float)
            h = Tools.calc_expression(h, float)
            
            calculo = a * b * h
            if calculo >= 0:
                Tools.resultado("Volume:", calculo, True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

        @staticmethod
        def volume_cilindro(raio, h, imprimir=False) -> float:
            if not Tools.trat_erro(float, [raio, h]):
                return None
            
            raio = Tools.calc_expression(raio, float)
            h = Tools.calc_expression(h, float)
            
            if raio < 0 or h < 0:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

            if os.getenv("SAIDA_PI") == 'True':
                raio = nsimplify(raio)
                h = nsimplify(h)
                calculo = pi * (raio**2) * h
                calculo = simplify(calculo)
                calculo = str(calculo).replace('*pi', 'π').replace('pi', 'π')
            else:
                calculo = math.pi * (raio**2) * h

            Tools.resultado("Volume:", calculo, aproximar=True if os.getenv("SAIDA_PI") == 'False' else False) if imprimir else None
            return calculo

        @staticmethod
        def volume_esfera(raio, imprimir=False) -> float:
            if not Tools.trat_erro(float, [raio]):
                return None
            
            raio = Tools.calc_expression(raio, float)
            
            if raio < 0:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None
            
            if os.getenv("SAIDA_PI") == 'True':
                raio = nsimplify(raio)
                calculo = (4 * pi * raio**3) / 3
                calculo = simplify(calculo)
                calculo = str(calculo).replace('*pi', 'π').replace('pi', 'π')
            else:
                calculo = (4/3) * math.pi * raio**3

            Tools.resultado("Volume:", calculo, aproximar=True if os.getenv("SAIDA_PI") == 'False' else False) if imprimir else None
            return calculo

        @staticmethod
        def volume_cone(raio, h, imprimir=False) -> float:
            if not Tools.trat_erro(float, [raio, h]):
                return None
            
            raio = Tools.calc_expression(raio, float)
            h = Tools.calc_expression(h, float)
            
            if raio < 0 or h < 0:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

            if os.getenv("SAIDA_PI") == 'True':
                raio = nsimplify(raio)
                h = nsimplify(h)
                calculo = (pi * (raio**2) * h) / 3
                calculo = simplify(calculo)
                calculo = str(calculo).replace('*pi', 'π').replace('pi', 'π')
            else:
                calculo = (math.pi * (raio**2) * h) / 3

            Tools.resultado("Volume:", calculo, aproximar=True if os.getenv("SAIDA_PI") == 'False' else False) if imprimir else None
            return calculo

        @staticmethod
        def volume_tronco_cone(R, r, h, imprimir=False) -> float:
            if not Tools.trat_erro(float, [R, r, h]):
                return None
            
            R = Tools.calc_expression(R, float)
            r = Tools.calc_expression(r, float)
            h = Tools.calc_expression(h, float)
            
            if R < 0 or r < 0 or h < 0:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

            if os.getenv("SAIDA_PI") == 'True':
                R = nsimplify(R)
                r = nsimplify(r)
                h = nsimplify(h)
                calculo = (pi * h * ((R**2) + (r**2) + (R*r))) / 3
                calculo = simplify(calculo)
                calculo = str(calculo).replace('*pi', 'π').replace('pi', 'π')
            else:
                calculo = (math.pi * h * ((R**2) + (r**2) + (R*r))) / 3

            Tools.resultado("Volume:", calculo, aproximar=True if os.getenv("SAIDA_PI") == 'False' else False) if imprimir else None
            return calculo