import msvcrt, os, time, math
# from sympy import pi

# Settings

casas_decimais = 2 
saida_angulo = "graus"
entrada_angulo = "graus"
saida_pi = False

pi = math.pi
euler = math.e

# Funções

RESET = '\033[0m'
WHITE = '\033[37m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
GRENN_BACKGROUND = '\033[42m'
RED_BACKGROUND = '\033[41m'


def clean():
    # Função para limpar a tela (compatível com Windows e Unix)
    os.system("cls" if os.name == "nt" else "clear")


def get_keypress():
    try:
        # Captura a tecla pressionada e tenta decodificar como UTF-8
        key = msvcrt.getch()
        decoded_key = key.decode('utf-8') if key else ''
    except UnicodeDecodeError:
        # Caso não consiga decodificar como UTF-8, usa ISO-8859-1 como alternativa
        decoded_key = key.decode('ISO-8859-1') if key else ''
    return decoded_key


def max_digits(lengh):
    return os.sys.set_int_max_str_digits(lengh)


def tratErro(tipo, parametros):
    for str_parametro in parametros:
        try:
            parametro = calcExpression(str_parametro)
            if tipo == float:
                float(parametro)
            elif tipo == int:
                int(parametro)
            elif tipo == str:
                str(parametro)
            else:
                ERROR(f"Erro: Tipo '{tipo}' não suportado para o valor '{parametro}'.")
                return False
        except (ValueError, TypeError) as e:
            ERROR(f"Erro: Verifique se o valor inserido está na forma correta: '{str_parametro}' ({e})")
            return False
    return True


def calcExpression(expressao, type=None):
    try:
        calculo = eval(expressao)
        if type == float:
            return float(calculo)
        elif type == int:
            return int(calculo)
        elif type == str:
            return str(calculo)
        elif type is None:
            return calculo
        else:
            print(f"Erro: Tipo '{type}' não suportado.")
            return None
    except (ValueError, TypeError, NameError) as e:
        ERROR(f"Erro ao resolver a expressão '{expressao}': {e}")
        return None


def voltar():
    input(RED + "Voltar(Enter)" + RESET)


def acaoInvalida():
    print(RED + "Favor selecionar uma ação válida." + RESET)
    time.sleep(1)


def resultado(texto, resultado=None, aproximar=None):
    if resultado:
        if aproximar:
            resultado = round(resultado, casas_decimais)
        print(GREEN + texto, str(resultado) + RESET)
    else:
        print(GREEN + texto + RESET)
    print("")


def ERROR(mensagem):
    print(RED + str("(ERROR) " + str(mensagem)) + RESET)
    print("")


# Não usado
def inserir(mensagem, tipo=None):
    if tipo == None:
        input(mensagem)
    else:
        try:
            if tipo == int:
                int(input(mensagem))
            elif tipo == float:
                float(input(mensagem))
            else:
                raise ValueError("Tipo não suportado")
        except ValueError:
            ERROR("Verifique se o valor inserido está na forma correta")