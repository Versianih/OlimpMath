from InquirerPy import prompt
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


def max_digits(lengh):
    # Função que determina a quantidade máxima de dígitos na saída
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
    voltar = [
        {
            "type": "list",
            "message": "",
            "choices": ["Voltar"],
        }
    ]
    prompt(voltar)


def acaoInvalida():
    print(RED + "Favor selecionar uma ação válida." + RESET)
    time.sleep(1)


def resultado(texto, resultado=None, aproximar=None, casas_decimais=casas_decimais):
    saida = []
    if resultado is not None:
        if isinstance(resultado, list) and aproximar is not None:
            for res in resultado:
                    res = round(res, casas_decimais)
                    saida.append(res)
            print(GREEN + texto, str(saida) + RESET)
        elif isinstance(resultado, list) and aproximar is None:
            print(GREEN + texto, str(resultado) + RESET)
        else:
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