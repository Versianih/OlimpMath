from functions.tools import Tools, math, euler


class Combinatoria:

    class Permutacao:
        def permutacao_n_em_k(n,k, imprimir=False) -> int:
            if not Tools.trat_erro(int, [n, k]):
                return None
            
            n = Tools.calc_expression(n, int)
            k = Tools.calc_expression(k, int)
            
            calculo = math.perm(n, k)
            Tools.resultado("Resultado:", calculo) if imprimir else None
            return calculo


        def permutacao_circular(n, imprimir=False) -> int:
            if not Tools.trat_erro(int, [n]):
                return None
        
            n = Tools.calc_expression(n, int)
        
            calculo = math.factorial((n-1))    
            Tools.resultado("Resultado:", calculo) if imprimir else None
            return calculo


        def permutacao_caotica(n, imprimir=False) -> int:
            if not Tools.trat_erro(int, [n]):
                return None
            
            n = Tools.calc_expression(n, int)
            
            if n >= 0:
                calculo = math.factorial(n)/euler
                calculoAproximado = int(round(calculo, 0))
                
                Tools.resultado("O resultado da permutação caótica é:", calculoAproximado, True) if imprimir else None
                return calculoAproximado
            else:
                Tools.ERROR("A quantidade de elementos não pode ser negativa") if imprimir else None


    class Combinacao:
        def combinacao(n, p, imprimir=False) -> int:
            if not Tools.trat_erro(int, [n, p]):
                return None
            
            n = Tools.calc_expression(n, int)
            p = Tools.calc_expression(p, int)
            
            if n >= 0 and p >= 0:
                calculo = math.factorial(n)/(math.factorial(p) * math.factorial(n-p))

                Tools.resultado("Resultado:", calculo) if imprimir else None
                return calculo
            else:
                Tools.ERROR("N e P não podem ser negativos") if imprimir else None


        def combinacao_completa(n, p, imprimir=False) -> int:
            if not Tools.trat_erro(int, [n, p]):
                return None
            
            n = Tools.calc_expression(n, int)
            p = Tools.calc_expression(p, int)
            if n >= 0 and p >= 0:
                calculo = math.factorial(n + (p - 1)) / (math.factorial(p) * math.factorial(n - 1))
                
                Tools.resultado("Resultado:", calculo, True) if imprimir else None
                return calculo
            else:
                Tools.ERROR("N ou P não pode ser negativo") if imprimir else None


    def fatorial(value, imprimir=False) -> int:
        if not Tools.trat_erro(int, [value]):
            return None

        value = Tools.calc_expression(value, int)
        
        if value >= 0:    
            calculo = math.factorial(value)
            
            Tools.resultado(f"Fatorial de {value} é:", calculo) if imprimir else None
            return calculo
        else:
            Tools.ERROR("O número não pode ser negativo") if imprimir else None