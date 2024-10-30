import msvcrt, os, time, math


pi = float("{:,.2f}".format(math.pi))

RED = '\033[31m'
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
GRENN_BACKGROUND = '\033[42m'

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

# Settings

casas_decimais = 2 
saida_angulo = "graus"
entrada_angulo = "graus"