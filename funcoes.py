import time, math, cmath


# Funções de Código{

pi = math.pi

def inserirFLOAT(mensagem):
    return float(input(mensagem))

def inserirINT(mensagem):
    return int(input(mensagem))

def voltar():
    input(RED + "Voltar(Enter)" + RESET)

def acaoInvalida():
    print(RED + "Favor selecionar uma ação válida." + RESET)
    time.sleep(1)

def resultado(resultado):
    print(GREEN + resultado + RESET)
    print("")
    
def ERROR(mensagem):
    print(RED + str("(ERROR)" + str(mensagem)) + RESET)
    print("")

RED = '\033[31m'
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
# }


# Funções de Geometria{
# Plana
def areaPoliRegular(qntLados, lado):
    if qntLados < 3:
        return "erro"
    elif qntLados == 3:
        Tricalculo = ((1 *((lado**2)*math.sqrt(3))) / 4)
        return "Área: " + str(Tricalculo)
    elif qntLados == 4:
        Quacalculo = lado**2
        return "Área: " + str(Quacalculo)
    else:
        calculo = ((qntLados * ((lado**2)*math.sqrt(3))) / 4)
        return "Área: " + str(calculo)        

def areaCírculo(raio):
    calculo = (raio*raio)* pi
    return "Área: " + str(calculo)


def areaQuadrado(lado):
    calculo = (lado*lado)
    return "Área: " + str(calculo)


def areaTriangulo(base, altura):
    calculo = (base*altura)/2
    return "Área: " + str(calculo)


def areaTrianguloHeron(a, b, c):
    p = (a + b + c)/2
    calculo = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return "Área: " + str(calculo) 


def areaTrapezio(BASE, base, altura):
    calculo = ((BASE+base)*altura)/2
    return "Área: " + str(calculo)

# Espacial
def areaCubo(lado):
    calculo = lado**3
    return "Área: " + str(calculo)

def areaParalelepipedo(a,b,h):
    calculo = (a*b*h)
    return "Área: " + str(calculo)

def areaCilindro(raio, h):
    calculo = (pi*(raio**2))*h
    return "Área: " + str(calculo)

def areaEsfera(raio):
    calculo = (4/3)*pi*raio
    return "Área: " + str(calculo)

# Analítica
def distPontos(xa, ya, xb, yb):
    calculo = (((xb - xa)**2) + ((yb - ya)**2))**(1/2)
    return "A Distância entre os Pontos é: " + str(calculo)
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
    return "Número na Base Decimal:" + str(decimal)
 
 
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
    return "Número na Base Final:" + str(numero_final)

def BaseParaBase(num_original,base_original,base_final):
    num_decimal = BaseParaDecimal(num_original,base_original)
    num_final = DecimalParaBase(num_decimal,base_final)
    return "Número na Base Final:" + str(num_final)
# }


# Funções de Álgebra {

def raizQuadrada(a):
    calculo = math.sqrt(a)
    return "Raiz: " + str(calculo)

def Resto(a, b):
    calculo = math.remainder(a,b)
    return "Resto: " + str(calculo)

def MDC(a,b):
    calculo = math.gcd(a,b)
    return "MDC: " + str(calculo)

def MMC(a, b):
    calculo = (abs(a*b))/(math.gcd(a,b))
    return "MMC: " + str(calculo)

def equação2Grau(a,b,c):
    if a != 0:    
        delta = b**2 -(4*a*c)
        if delta >= 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            return "As Raizes da Equação são: " + str(((x1), (x2)))
        else:
            cx1 = (-b + cmath.sqrt(delta))/(2*a)
            cx2 = (-b - cmath.sqrt(delta))/(2*a)
            return "As Raizes Complexas da Equação são: " + str(((cx1), (cx2)))
    else:
        return "'a' tem que ser diferente de 0"

# }


# Funções de Trigonometria {

def HipotenusaComOposto(a,b):
    ang = math.radians(b)
    hipotenusa = a/(math.sin(ang))
    return "Hipotenusa: " + str(hipotenusa)

def HipotenusaComAdjacente(a,b):
    ang = math.radians(b)
    hipotenusa = a/(math.cos(ang))
    return "Hipotenusa: " + str(hipotenusa)


def OpostoComHipotenusa(a,b):
    ang = math.radians(b)
    oposto = a*(math.sin(ang))
    return "Cateto Oposto: " + str(oposto)

def OpostoComAdjacente(a,b):
    ang = math.radians(b)
    oposto = a*(math.tan(ang))
    return "Cateto Oposto: " + str(oposto)


def AdjacenteComHipotenusa(a,b):
    ang = math.radians(b)
    adjacente = a*(math.cos(ang))
    return "Cateto Adjacente: " + str(adjacente)

def AdjacenteComOposto(a,b):
    ang = math.radians(b)
    adjacente = a/(math.tan(ang))
    return "Cateto Adjacente: " + str(adjacente)


def AnguloComCOCA(a,b): #a=CO b=CA
    ang_rad = math.atan(a/b)
    angulo = math.degrees(ang_rad)
    return "Ângulo: " + str(angulo)

def AnguloComCOH(a,b): #a=CO b=H
    print(a,b)
    apb = (a/b)
    ang_rad = math.asin(apb)
    print(ang_rad)
    angulo = math.degrees(ang_rad)
    return "Ângulo: " + str(angulo) 

def AnguloComCAH(a,b): #a=CA b=H
    ang_rad = math.acos(a/b)
    angulo = math.degrees(ang_rad)
    return "Ângulo: " + str(angulo)
# }


# Combinatória{

def PermutaçãoDeNemK(n,k):
    calculo = math.perm(n, k)
    return "Resultado: " + str(calculo)

def PermutaçãoCircular(n):
    calculo = math.factorial((n-1))
    return "Resultado: " + str(calculo)

def Combinação(n,k):
    calculo = math.comb(n,k)
    return "Resultado: " + str(calculo)

def Fatorial(n):
    calculo = math.factorial(n)
    return "Fatorial desse Número é: " + str(calculo)
# }