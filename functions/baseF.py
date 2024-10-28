from functions.functions import tratErro, resultado, ERROR


def BaseParaDecimal(num_original,base_original):
    if tratErro(int, [num_original, base_original]) == True:
        num_original = str(num_original)
        base_original = int(base_original)
        
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        decimal = 0
        decimal_temp = list(num_original)
        decimal_temp.reverse()
        for x,i in enumerate(decimal_temp):
            decimal += dic.index(i) * base_original**(x)
        return resultado("Número na Base Decimal:" + str(decimal))
 
 
def DecimalParaBase(decimal,base_final):
    if tratErro(int, [base_final, decimal]) == True:
        base_final = int(base_final)
        decimal = int(decimal)
        
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
        return resultado("Número na Base Final:" + str(numero_final))


def BaseParaBase(num_original,base_original,base_final):
    if tratErro(int, [num_decimal, base_original, base_final]) == True:
        num_decimal = int(num_decimal)
        base_final = int(base_final)
        base_original = int(base_original)

        num_decimal = BaseParaDecimal(num_original,base_original)
        num_final = DecimalParaBase(num_decimal,base_final)
        return resultado("Número na Base Final:" + str(num_final))