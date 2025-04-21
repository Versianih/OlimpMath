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

    @staticmethod
    def clean():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def max_digits(lengh):
        return os.sys.set_int_max_str_digits(lengh)

    @staticmethod
    def trat_erro(tipo:type, parametros:list) -> bool:
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

    @staticmethod
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
            return False

    @staticmethod
    def voltar():
        voltar = [
            {
                "type": "list",
                "message": "",
                "choices": ["Voltar"],
            }
        ]
        prompt(voltar)

    @staticmethod
    def resultado(texto:str, resultado:int|float=None, aproximar:bool=False) -> None:
        load_dotenv()
        CASAS_DECIMAIS = int(os.getenv('CASAS_DECIMAIS', 2))
        
        if resultado is None:
            print(f"{GREEN}{texto}{RESET}")
            return
            
        if isinstance(resultado, list) and aproximar is not False:
            saida = [round(res, CASAS_DECIMAIS) for res in resultado]
            print(f"{GREEN}{texto} {saida}{RESET}")
        elif isinstance(resultado, list):
            print(f"{GREEN}{texto} {resultado}{RESET}")
        else:
            if aproximar:
                resultado = round(resultado, CASAS_DECIMAIS)
            print(f"{GREEN}{texto} {resultado}{RESET}")

    @staticmethod
    def ERROR(mensagem:str = ""):
        print(f"{RED}(ERROR) {mensagem}{RESET}")