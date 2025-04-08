from InquirerPy import prompt
from functions.tools import Tools
from functions.geoFunctions.geoPlanaF import (
    area_poligono_regular,
    area_circulo,
    area_quadrado,
    area_trapezio,
    area_triangulo,
    area_triangulo_heron,
    
    # Pitágoras
    pitagoras_hipotenusa,
    pitagoras_cateto,
    
    # Formação de Triângulos
    formacao_triangulo,
)


def geometria_plana():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA",
                "choices": ["Áreas", "Polígonos", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Áreas
        if escolha == "Áreas":
            geometria_plana_areas()
        
        # Pitágoras
        elif escolha == "Polígonos":
            geometria_plana_poligonos()
        
        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def geometria_plana_areas():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> ÁREAS",
                "choices": ["Polígono Regular", "Círculo", "Quadrado", "Triângulo +", "Trapézio", "Voltar"],
            }
        ]

        escolha = prompt(campos)
        escolha = escolha.get(0)
        
        # Polígono Regular Qualquer
        if escolha == "Polígono Regular":
            Tools.clean()
            area_poligono_regular(input("Quantidade de Lados do Polígono:"), input("Medida do Lado do Polígono:"), True)
            Tools.voltar()

        # Círculo
        elif escolha == "Círculo":
            Tools.clean()
            area_circulo(input("Raio do Círculo:"), True)
            Tools.voltar()

        # Quadrado
        elif escolha == "Quadrado":
            Tools.clean()
            area_quadrado(input("Lado do Quadrado:"), True)
            Tools.voltar()

        # Triângulo
        elif escolha == "Triângulo +":
            Tools.clean()
            campos_triangulo = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> ÁREAS -> ÁREA TRIÂNGULO",
                "choices": ["Base e Altura", "Fórmula de Heron", "Voltar"],
                }
            ]
            escolha_triangulo = prompt(campos_triangulo)
            escolha_triangulo = escolha_triangulo.get(0)

            if escolha_triangulo == "Base e Altura":  # Base e Altura
                Tools.clean()
                area_triangulo(input("Base do triagulo:"), input("Altura do triagulo:"), True)
                Tools.voltar()

            elif escolha_triangulo == "Fórmula de Heron":  # Fórmula de Heron
                Tools.clean()
                area_triangulo_heron(input("Lado 1 do Triângulo:"), input("Lado 2 do Triângulo:"), input("Lado 3 do Triângulo:"), True)
                
                Tools.voltar()

            elif escolha_triangulo == "Tools.Voltar":
                Tools.clean()
                pass

        # Trapézio
        elif escolha == "Trapézio":
            Tools.clean()
            area_trapezio(input("Base1 do Trapézio:"), input("Base2 do Trapézio:"), input("Altura do Trapézio:"), True)
            Tools.voltar()
        
        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def geometria_plana_poligonos():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> POLÍGONOS",
                "choices": ["Triângulo +", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Triângulos
        if escolha == "Triângulo +":
            Tools.clean()
            geometria_plana_poligonos_triangulo()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def geometria_plana_poligonos_triangulo():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> POLÍGONOS -> TRIÂNGULO",
                "choices": ["Pitágoras +", "Formação de Triângulo", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)


        # Teorema de Pitágoras
        if escolha == "Pitágoras +": 
            Tools.clean()
            geometria_plana_poligonos_triangulo_pitagoras()

        # Formação de Triângulos
        elif escolha == "Formação de Triângulo":
            Tools.clean()
            formacao_triangulo(input("Lado 1 do Triângulo:"), input("Lado 2 do Triângulo:"), input("Lado 3 do Triângulo:"), True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def geometria_plana_poligonos_triangulo_pitagoras():
    while True:
        Tools.clean()
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> POLÍGONOS -> TRIÂNGULO -> TEOREMA DE PITÁGORAS",
                "choices": ["Calcular Hipotenusa", "Calcular Cateto", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Teorema de Pitágoras para descobrir a Hipotenusa
        if escolha == "Calcular Hipotenusa":
            Tools.clean()
            pitagoras_hipotenusa(input("Cateto:"), input("Cateto:"), True)
            Tools.voltar()

        # Teorema de Pitágoras para descobrir o Cateto
        elif escolha == "Calcular Cateto":
            Tools.clean()
            pitagoras_cateto(input("Cateto:"), input("Hipotenusa:"), True)
            Tools.voltar()

        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break