from functions.tools import Tools

class Geometria_Analitica:

    @staticmethod
    def distancia_entre_pontos(xa, ya, xb, yb, imprimir=False) -> float:
        if not Tools.trat_erro(float, [xa, ya, xb, yb]):
            return None
        
        xa = Tools.calc_expression(xa, float)
        ya = Tools.calc_expression(ya, float)
        xb = Tools.calc_expression(xb, float)
        yb = Tools.calc_expression(yb, float)
        
        calculo = (((xb - xa)**2) + ((yb - ya)**2))**(1/2)
        if calculo >= 0:    
            Tools.resultado("A Distância entre os Pontos é:", calculo, True) if imprimir else None
            return calculo
        else:
            Tools.ERROR("Distância não pode ser negativa") if imprimir == True else None

    @staticmethod
    def retangulos_em_uma_malha(n, m, imprimir=False) -> int: 
        if not Tools.trat_erro(int, [n, m]):
            return None

        n = Tools.calc_expression(n, int)
        m = Tools.calc_expression(m, int)
        
        retangulos = (m * n * (n + 1) * (m + 1)) // 4
        Tools.resultado(f"A quantidade de retângulos possíveis em uma malha {n}x{m} é de: {retangulos} retângulos") if imprimir else None
        return retangulos 