from InquirerPy import prompt
import os, math
from dotenv import load_dotenv

# Settings

casas_decimais = 2 
saida_angulo = "graus"
entrada_angulo = "graus"
saida_pi = False

pi = math.pi
euler = math.e

RESET = '\033[0m'
WHITE = '\033[37m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
GRENN_BACKGROUND = '\033[42m'
RED_BACKGROUND = '\033[41m'

class Tools:
    def clean():
        # Função para limpar a tela (compatível com Windows e Unix)
        os.system("cls" if os.name == "nt" else "clear")


    def max_digits(lengh):
        # Função que determina a quantidade máxima de dígitos na saída
        return os.sys.set_int_max_str_digits(lengh)


    def trat_erro(tipo, parametros):
        for str_parametro in parametros:
            try:
                parametro = Tools.calc_expression(str_parametro)
                if tipo == float:
                    float(parametro)
                elif tipo == int:
                    int(parametro)
                elif tipo == str:
                    str(parametro)
                else:
                    Tools.ERROR(f"Erro: Tipo '{tipo}' não suportado para o valor '{parametro}'.")
                    return False
            except (ValueError, TypeError) as e:
                Tools.ERROR(f"Erro: Verifique se o valor inserido está na forma correta: '{str_parametro}' ({e})")
                return False
        return True


    def calc_expression(expressao, type=None):
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
            Tools.ERROR(f"Erro ao resolver a expressão '{expressao}': {e}")
            return None


    def voltar(self):
        voltar = [
            {
                "type": "list",
                "message": "",
                "choices": ["Voltar"],
            }
        ]
        prompt(voltar)


    def resultado(texto, resultado=None, aproximar=None):
        load_dotenv()
        CASAS_DECIMAIS = os.getenv('casas_decimais')
        saida = []
        if resultado is not None:
            if isinstance(resultado, list) and aproximar is not None:
                for res in resultado:
                        res = round(res, CASAS_DECIMAIS)
                        saida.append(res)
                print(GREEN + texto, str(saida) + RESET)
            elif isinstance(resultado, list) and aproximar is None:
                print(GREEN + texto, str(resultado) + RESET)
            else:
                if aproximar:
                    resultado = round(resultado, CASAS_DECIMAIS)
                print(GREEN + texto, str(resultado) + RESET)
        else:
            print(GREEN + texto + RESET)
        print("")


    def ERROR(mensagem):
        print(RED + str("(ERROR) " + str(mensagem)) + RESET)
        print("")