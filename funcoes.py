import math

# Funções de Código{
pi = math.pi

def inserir(mensagem):
    return float(input(mensagem))

def voltar():
    x = RED + "Voltar(Enter)" + RESET
    return x

RED = '\033[31m'
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'


# }
# Funções de Áreas{
def areaCírculo(raio):
    calculo = (raio*raio)* pi
    return calculo


def areaQuadrado(lado):
    calculo = (lado*lado)
    return calculo


def areaTriangulo(base, altura):
    calculo = (base*altura)/2
    return calculo


def areaTrianguloHeron(a, b, c):
    p = (a + b + c)/2
    calculo = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return calculo 


def areaTrapezio(BASE, base, altura):
    calculo = ((BASE+base)*altura)/2
    return calculo
# }


# Funções de Bases{
def BaseParaDecimal(num_original,base_original):
    num_original = str(num_original)
    base_original = int(base_original)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    decimal = 0
    decimal_temp = list(num_original)
    decimal_temp.reverse()
    for x,i in enumerate(decimal_temp):
        decimal += dic.index(i) * base_original**(x)
    return str(decimal)
 
 
def DecimalParaBase(decimal,base_final):
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
    return numero_final

def BaseParaBase(num_original,base_original,base_final):
    num_decimal = BaseParaDecimal(num_original,base_original)
    num_final = DecimalParaBase(num_decimal,base_final)
    return num_final

# }

# Funções de Álgebra {

def raizQuadrada(a):
    calculo = math.sqrt(a)
    return calculo

def Resto(a, b):
    calculo = math.remainder(a,b)
    return calculo

def MDC(a,b):
    calculo = math.gcd(a,b)
    return calculo

# }

# Funções de Trigonometria {

def HipotenusaComOposto(a,b):
    hipotenusa = a/(math.sin(b))
    return hipotenusa

def HipotenusaComAdjacente(a,b):
    hipotenusa = a/(math.cos(b))
    return hipotenusa


def OpostoComHipotenusa(a,b):
    oposto = a*(math.sin(b))
    return oposto

def OpostoComAdjacente(a,b):
    oposto = a*(math.tan(b))
    return oposto


def AdjacenteComHipotenusa(a,b):
    adjacente = a*(math.cos(b))
    return adjacente

def AdjacenteComOposto(a,b):
    adjacente = a/(math.tan(b))
    return adjacente


def AnguloComCOCA(a,b): #a=CO b=CA
    ang_rad = math.atan(a/b)
    angulo = math.degrees(ang_rad)
    return angulo

def AnguloComCOH(a,b): #a=CO b=H
    ang_rad = math.asin(a/b)
    angulo = math.degrees(ang_rad)
    return angulo 

def AnguloComCAH(a,b): #a=CA b=H
    ang_rad = math.acos(a/b)
    angulo = math.degrees(ang_rad)
    return angulo
# }