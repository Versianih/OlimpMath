from functions.tools import Tools, math, pi

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
            
            calculo = (pi * (raio**2)) * h
            if calculo >= 0:
                Tools.resultado("Volume:", calculo, True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

        @staticmethod
        def volume_esfera(raio, imprimir=False) -> float:
            if not Tools.trat_erro(float, [raio]):
                return None
            
            raio = Tools.calc_expression(raio, float)
            
            calculo = (4/3) * pi * raio**3
            if calculo >= 0:    
                Tools.resultado("Volume:", calculo, aproximar=True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

        @staticmethod
        def volume_cone(raio, h, imprimir=False) -> float:
            if not Tools.trat_erro(float, [raio, h]):
                return None
            
            raio = Tools.calc_expression(raio, float)
            h = Tools.calc_expression(h, float)
            
            calculo = (pi * (raio**2) * h) / 3
            if calculo >= 0:
                Tools.resultado("Volume:", calculo, aproximar=True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None

        @staticmethod
        def volume_tronco_cone(R, r, h, imprimir=False) -> float:
            if not Tools.trat_erro(float, [R, r, h]):
                return None
            
            R = Tools.calc_expression(R, float)
            r = Tools.calc_expression(r, float)
            h = Tools.calc_expression(h, float)
            
            calculo = (pi * h * ((R**2) + (r**2) + (R*r))) / 3
            if calculo >= 0:    
                Tools.resultado("Volume:", calculo, aproximar=True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("Volume não pode ser negativo") if imprimir else None
                return None