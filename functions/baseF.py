from functions.functions import tratErro, resultado, ERROR, calcExpression


def BaseParaDecimal(num_original, base_original, print=None):
    if tratErro(int, [num_original, base_original]):
        num_original = calcExpression(num_original, str)
        base_original = calcExpression(base_original, int)
        
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        decimal = 0
        decimal_temp = list(num_original)
        decimal_temp.reverse()
        for x,i in enumerate(decimal_temp):
            decimal += dic.index(i) * base_original**(x)
        if print == True:
            resultado("Número na Base Decimal:", decimal)
        return decimal

 
def DecimalParaBase(decimal, base_final, print=None):
    if tratErro(int, [base_final, decimal]) == True:
        base_final = calcExpression(base_final, int)
        decimal = calcExpression(decimal, int)
        
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
        if print == True:
            resultado("Número na Base Final:", numero_final)
        return numero_final


def BaseParaBase(num_original,base_original,base_final, print=None):
    if tratErro(int, [num_original, base_original, base_final]) == True:
        num_original = calcExpression(num_original, int)
        base_final = calcExpression(base_final, int)
        base_original = calcExpression(base_original, int)

        num_decimal = BaseParaDecimal(num_original,base_original)
        num_final = DecimalParaBase(num_decimal,base_final)
        if print == True:
            resultado("Número na Base Final:", num_final)
        return num_final