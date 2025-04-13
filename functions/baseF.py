from functions.tools import Tools

class Base:

    @staticmethod
    def base_para_decimal(num_original, base_original, imprimir = False) -> int:
        if not Tools.trat_erro(int, [base_original]):
            return None
        
        base_original = Tools.calc_expression(base_original, int)
        
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        for char in num_original:
            if char.upper() not in dic[:base_original]:
                return None
        
        decimal = 0
        decimal_temp = list(num_original.upper())
        decimal_temp.reverse()
        
        for x, i in enumerate(decimal_temp):
            decimal += dic.index(i.upper()) * (base_original ** x)
        
        
        Tools.resultado("Número na Base Decimal:", decimal) if imprimir else None 
        
        return decimal
    
    @staticmethod
    def decimal_para_base(decimal, base_final, imprimir = False) -> str:
        if not Tools.trat_erro(int, [base_final, decimal]):
            return None
        
        base_final = Tools.calc_expression(base_final, int)
        decimal = Tools.calc_expression(decimal, int)
        
        if base_final < 2 or base_final > 36:
            return None
        
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        if decimal == 0:
            numero_final = '0'
        else:
            numero_final_temp = []
            numero_final = ''
            
            while decimal > 0:
                temp_numero_final = decimal % base_final
                numero_final_temp.append(temp_numero_final)
                decimal = decimal // base_final
            
            numero_final_temp.reverse()
            for i in numero_final_temp:
                numero_final += dic[i]
        
        
        Tools.resultado("Número na Base Final:", numero_final) if imprimir else None
        
        return numero_final
    
    @staticmethod
    def base_para_base(num_original, base_original, base_final, imprimir = False) -> str:
        if not Tools.trat_erro(int, [base_original, base_final]):
            return None
        
        base_final = Tools.calc_expression(base_final, int)
        base_original = Tools.calc_expression(base_original, int)

        if base_original < 2 or base_original > 36 or base_final < 2 or base_final > 36:
            return None
        
        num_decimal = Base.base_para_decimal(str(num_original), str(base_original))
        
        if num_decimal is None:
            return None
            
        num_final = Base.decimal_para_base(str(num_decimal), str(base_final))
        

        Tools.resultado("Número na Base Final:", num_final) if imprimir else None
        
        return num_final