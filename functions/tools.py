from InquirerPy import prompt
import os, math
from dotenv import load_dotenv

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
        os.system("cls" if os.name == "nt" else "clear")


    def max_digits(lengh):
        return os.sys.set_int_max_str_digits(lengh)

    def trat_erro(tipo, parametros):
        if tipo not in (float, int, str):
            Tools.ERROR(f"Erro: Tipo '{tipo}' não suportado.")
            return False
            
        for str_parametro in parametros:
            try:
                parametro = Tools.calc_expression(str_parametro)
                tipo(parametro)
            except (ValueError, TypeError) as e:
                Tools.ERROR(f"Erro: Verifique se o valor inserido está na forma correta: '{str_parametro}' ({e})")
                return False
        return True


    def calc_expression(expressao, type=None):
        try:
            resposta = eval(expressao, {"__builtins__": {}})
            
            if type in (float, int, str):
                return type(resposta)
            elif type is None:
                return resposta
            else:
                print(f"Erro: Tipo '{type}' não suportado.")
                return None
        except Exception as e:
            Tools.ERROR(f"Erro ao resolver a expressão '{expressao}': {e}")
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


    def resultado(texto, resultado=None, aproximar=False):
        load_dotenv()
        CASAS_DECIMAIS = int(os.getenv('CASAS_DECIMAIS'))
        
        if resultado is None:
            print(f"{GREEN}{texto}{RESET}\n")
            return
            
        if isinstance(resultado, list) and aproximar is not False:
            saida = [round(res, CASAS_DECIMAIS) for res in resultado]
            print(f"{GREEN}{texto} {saida}{RESET}\n")
        elif isinstance(resultado, list):
            print(f"{GREEN}{texto} {resultado}{RESET}\n")
        else:
            if aproximar:
                resultado = round(resultado, CASAS_DECIMAIS)
            print(f"{GREEN}{texto} {resultado}{RESET}\n")


    def ERROR(mensagem):
        print(RED + str("(ERROR) " + str(mensagem)) + RESET)
        print("")