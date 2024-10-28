import msvcrt, os, time, math


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