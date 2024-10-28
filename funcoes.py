import msvcrt, os, time, math

# Funções de Código{
pi = float("{:,.2f}".format(math.pi))

def clean():
    # Função para limpar a tela (compatível com Windows e Unix)
    os.system("cls" if os.name == "nt" else "clear")

def get_keypress():
    return msvcrt.getch().decode('utf-8')

def max_digits(lengh):
    return os.sys.set_int_max_str_digits(lengh)

def tratErro(tipo, parametros):
    for parametro in parametros:
        try:
            if tipo == float:
                float(parametro)
            elif tipo == int:
                int(parametro)
            elif tipo == str:
                str(parametro)
            else:
                raise ValueError("Tipo não suportado")
        except ValueError:
            ERROR("Verifique se o valor inserido está na forma correta: {}".format(parametro))
            return False
    return True

def voltar():
    input(RED + "Voltar(Enter)" + RESET)

def acaoInvalida():
    print(RED + "Favor selecionar uma ação válida." + RESET)
    time.sleep(1)

def resultado(resultado):
    print(GREEN + resultado + RESET)
    print("")
    
def ERROR(mensagem):
    print(RED + str("(ERROR) " + str(mensagem)) + RESET)
    print("")

RED = '\033[31m'
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
# }


# Funções de Geometria{
# Plana
def areaPoliRegular(qntLados, lado):
    if tratErro(int, [qntLados]) & tratErro(float, [lado]) == True:    
        qntLados = int(qntLados)
        lado = float(lado)
        if qntLados < 3:
            return ERROR("Verifique se a quantidade de lados permite um Polígono")
        elif qntLados == 3:
            Tricalculo = ((1 *((lado**2)*math.sqrt(3))) / 4)
            if Tricalculo >= 0:
                return resultado("Área: " + str(Tricalculo))
            else:
                return ERROR("Área não pode ser negativa")
        elif qntLados == 4:
            Quacalculo = lado**2
            if Quacalculo >= 0:
                return resultado("Área: " + str(Quacalculo))
            else:
                return ERROR("Área não pode ser negativa")
        else:
            calculo = ((qntLados * ((lado**2)*math.sqrt(3))) / 4)
            if calculo >= 0:    
                return resultado("Área: " + str(calculo))        
            else:
                return ERROR("Área não pode ser negativa")


def areaCírculo(raio):
    if tratErro(float, [raio]) == True:
        raio = float(raio)
        calculo = (raio*raio)* pi
        if calculo >= 0:
            return resultado("Área: " + str(calculo))
        else:
            return ERROR("Área não pode ser negativa")

def areaQuadrado(lado):
    if tratErro(float, [lado]) == True:
        lado = float(lado)
        calculo = (lado*lado)
        if calculo >= 0:
            return resultado("Área: " + str(calculo))
        else:
            return ERROR("Área não pode ser negativa")

def areaTriangulo(base, altura):
    if tratErro(float, [base, altura]) == True:    
        base = float(base)
        altura = float(altura)
        calculo = (base*altura)/2   
        if calculo >= 0:    
            return resultado("Área: " + str(calculo))
        else:    
            return ERROR("Área não pode ser negativa")

def areaTrianguloHeron(a, b, c):
    if tratErro(float, [a, b, c]) == True:    
        a = float(a)
        b = float(b)
        c = float(c)
        p = (a + b + c)/2
        calculo = math.sqrt(p*(p-a)*(p-b)*(p-c))
        if calculo >= 0:
            return resultado("Área: " + str(calculo)) 
        else:
            return ERROR("Área não pode ser negativa")

def areaTrapezio(BASE, base, altura):
    if tratErro(float, [BASE, base, altura]) == True:    
        BASE = float(BASE)
        base = float(base)
        altura = float(altura)
        calculo = ((BASE+base)*altura)/2
        if calculo >= 0:
            return resultado("Área: " + str(calculo))
        else:
            return ERROR("Área não pode ser negativa")


# Espacial
def volumePrisma(qntlados, lado, altura):
    if tratErro(int, qntlados) & tratErro(float, [lado, altura]) == True:
        qntlados = int(qntlados)
        lado = float(lado)        
        altura = float(altura)
        if qntlados < 3:
            return ERROR("Verifique se a quantidade de lados permite a base")
        elif qntlados == 3:
            base = ((1 *((lado**2)*math.sqrt(3))) / 4)
        elif qntlados == 4:
            base = lado**2
        else:
            base = ((qntlados * ((lado**2)*math.sqrt(3))) / 4)
        calculo = base*altura
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")

def volumeCubo(lado):
    if tratErro(float, [lado]) == True:
        lado = float(lado)
        calculo = lado**3
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")

def volumeParalelepipedo(a,b,h):
    if tratErro(float, [a, b, h]) == True:
        a = float(a)
        b = float(b)
        h = float(h)
        calculo = (a*b*h)
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")

def volumeCilindro(raio, h):
    if tratErro(float, [raio, h]) == True:    
        raio = float(raio)
        h = float(h)
        calculo = (pi*(raio**2))*h
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")

def volumeEsfera(raio):
    if tratErro(float, [raio]) == True:
        raio = float(raio)    
        calculo = (4/3)*pi*raio
        if calculo >= 0:    
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")

def volumeCone(raio, h):
    if tratErro(float, [raio, h]) == True:
        raio = float(raio)
        h = float(h)
        calculo = (pi*(raio**2)*h)/3
        if calculo >= 0:
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")

def volumeTroncoCone(R, r, h):
    if tratErro(float, [R, r, h]) == True:
        R = float(R)
        r = float(r)
        h = float(h)
        calculo = (pi*h*((R**2)+(r**2)+(R*r)))/3
        if calculo >= 0:    
            return resultado("Volume: " + str(calculo))
        else:
            return ERROR("Volume não pode ser negativo")
        

# Analítica
def distPontos(xa, ya, xb, yb):
    if tratErro(float, [xa, ya, xb, yb]) == True:
        xa = float(xa)
        ya = float(ya)
        xb = float(xb)
        yb = float(yb)
        calculo = (((xb - xa)**2) + ((yb - ya)**2))**(1/2)
        if calculo >= 0:    
            return resultado("A Distância entre os Pontos é: " + str(calculo))
        else:
            return ERROR("Distância não pode ser negativa")
# }


# Funções de Bases{
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
# }


# Funções de Álgebra {

def raizQuadrada(a):
    if tratErro(float, [a]) == True:
        a = float(a)    
        calculo = (a)**(1/2)
        return resultado("Raiz: " + str(calculo))

def Resto(a, b):
    if tratErro(float, [a, b]) == True:    
        a = float(a)
        b = float(b)
        calculo = math.remainder(a,b)
        return resultado("Resto: " + str(calculo))

def MDC(a,b):
    if tratErro(int, [a, b]) == True:    
        a = int(a)
        b = int(b)
        calculo = math.gcd(a,b)
        return resultado("MDC: " + str(calculo))

def MMC(a, b):
    if tratErro(int, [a, b]) == True:    
        a = int(a)
        b = int(b)
        calculo = (abs(a*b))/(math.gcd(a,b))
        return resultado("MMC: " + str(calculo))

def equação2Grau(a,b,c):
    if tratErro(float, [a, b, c]) == True:
        a = float(a)
        b = float(b)
        c = float(c)
        if a != 0:    
            delta = b**2 - (4*a*c)
            if delta >= 0:
                x1 = (-b + (delta**(1/2)))/(2*a)
                x2 = (-b - (delta**(1/2)))/(2*a)
                return resultado("As Raizes da Equação são: " + str(((x1), (x2))))
            else:
                cx1 = (-b + (delta**(1/2)))/(2*a)
                cx2 = (-b - (delta**(1/2)))/(2*a)
                return resultado("As Raizes Complexas da Equação são: " + str(((cx1), (cx2))))
        else:
            return ERROR("'a' tem que ser diferente de 0")

# }


# Funções de Trigonometria {

def HipotenusaComOposto(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)    
        ang = math.radians(b)
        hipotenusa = a/(math.sin(ang))
        return resultado("Hipotenusa: " + str(hipotenusa))

def HipotenusaComAdjacente(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        hipotenusa = a/(math.cos(ang))
        return resultado("Hipotenusa: " + str(hipotenusa))


def OpostoComHipotenusa(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        oposto = a*(math.sin(ang))
        return resultado("Cateto Oposto: " + str(oposto))

def OpostoComAdjacente(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        oposto = a*(math.tan(ang))
        return resultado("Cateto Oposto: " + str(oposto))


def AdjacenteComHipotenusa(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        adjacente = a*(math.cos(ang))
        return resultado("Cateto Adjacente: " + str(adjacente))

def AdjacenteComOposto(a,b):
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang = math.radians(b)
        adjacente = a/(math.tan(ang))
        return resultado("Cateto Adjacente: " + str(adjacente))


def AnguloComCOCA(a,b): #a=CO b=CA
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang_rad = math.atan(a/b)
        angulo = math.degrees(ang_rad)
        return resultado("Ângulo: " + str(angulo))

def AnguloComCOH(a,b): #a=CO b=H
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang_rad = math.asin(a/b)
        angulo = math.degrees(ang_rad)
        return resultado("Ângulo: " + str(angulo)) 

def AnguloComCAH(a,b): #a=CA b=H
    if tratErro(float, [a, b]) == True:
        a = float(a)
        b = float(b)
        ang_rad = math.acos(a/b)
        angulo = math.degrees(ang_rad)
        return resultado("Ângulo: " + str(angulo))
# }


# Combinatória{

def PermutaçãoDeNemK(n,k):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)    
        calculo = math.perm(n, k)
        return resultado("Resultado: " + str(calculo))

def PermutaçãoCircular(n):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial((n-1))
        return resultado("Resultado: " + str(calculo))

def Combinação(n,k):
    if tratErro(int, [n, k]) == True:
        n = int(n)
        k = int(k)
        calculo = math.comb(n,k)
        return resultado("Resultado: " + str(calculo))

def Fatorial(n):
    if tratErro(int, [n]) == True:
        n = int(n)
        calculo = math.factorial(n)
        return resultado("Fatorial desse Número é: " + str(calculo))
# }