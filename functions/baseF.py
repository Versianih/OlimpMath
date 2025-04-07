from functions.functions import trat_erro, resultado, calc_expression


def base_para_decimal(num_original, base_original, imprimir=False):
    if trat_erro(int, [num_original, base_original]):
        num_original = calc_expression(num_original, str)
        base_original = calc_expression(base_original, int)
        
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        decimal = 0
        decimal_temp = list(num_original)
        decimal_temp.reverse()
        for x,i in enumerate(decimal_temp):
            decimal += dic.index(i) * base_original**(x)

        resultado("Número na Base Decimal:", decimal) if imprimir else None
        return decimal

 
def decimal_para_base(decimal, base_final, imprimir=False):
    if trat_erro(int, [base_final, decimal]):
        base_final = calc_expression(base_final, int)
        decimal = calc_expression(decimal, int)
        
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numero_final_temp = []
        numero_final = ''
        while True:
            temp_numero_final = decimal%base_final
            numero_final_temp.append(temp_numero_final)
            if int(decimal/base_final) == 0:
                break
            decimal = int(decimal/base_final)
        numero_final_temp.reverse()
        for i in numero_final_temp:
            numero_final += dic[i]

        resultado("Número na Base Final:", numero_final) if imprimir else None
        return numero_final


def base_para_base(num_original,base_original,base_final, imprimir=False):
    if trat_erro(int, [num_original, base_original, base_final]):
        num_original = calc_expression(num_original, int)
        base_final = calc_expression(base_final, int)
        base_original = calc_expression(base_original, int)

        num_decimal = base_para_decimal(num_original,base_original)
        num_final = decimal_para_base(num_decimal,base_final)

        resultado("Número na Base Final:", num_final) if imprimir else None
        return num_final