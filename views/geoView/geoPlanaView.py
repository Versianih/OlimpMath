from InquirerPy import prompt
from functions.functions import (
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from functions.geoFunctions.geoPlanaF import (
    areaPoliRegular,
    areaCírculo,
    areaQuadrado,
    areaTrapezio,
    areaTriangulo,
    areaTrianguloHeron,
    # Pitágoras
    pitagorasHipotenusa,
    pitagorasCateto,
    # Formação de Triângulos
    formaçãoTriângulo,
)


def geometriaPlana():
    while True:
        clean()
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
            geoPlanaAreas()
        
        # Pitágoras
        elif escolha == "Polígonos":
            geoPlanaPoligonos()
        
        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def geoPlanaAreas():
    while True:
        clean()
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
            clean()
            areaPoliRegular(input("Quantidade de Lados do Polígono:"), input("Medida do Lado do Polígono:"), True)
            voltar()

        # Círculo
        elif escolha == "Círculo":
            clean()
            areaCírculo(input("Raio do Círculo:"), True)
            voltar()

        # Quadrado
        elif escolha == "Quadrado":
            clean()
            areaQuadrado(input("Lado do Quadrado:"), True)
            voltar()

        # Triângulo
        elif escolha == "Triângulo +":
            clean()
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
                clean()
                areaTriangulo(input("Base do triagulo:"), input("Altura do triagulo:"), True)
                voltar()

            elif escolha_triangulo == "Fórmula de Heron":  # Fórmula de Heron
                clean()
                areaTrianguloHeron(input("Lado 1 do Triângulo:"), input("Lado 2 do Triângulo:"), input("Lado 3 do Triângulo:"), True)
                voltar()

            elif escolha_triangulo == "Voltar":
                clean()
                pass
            else:
                acaoInvalida()

        # Trapézio
        elif escolha == "Trapézio":
            clean()
            areaTrapezio(input("Base1 do Trapézio:"), input("Base2 do Trapézio:"), input("Altura do Trapézio:"), True)
            voltar()
        
        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()

def geoPlanaPoligonos():
    while True:
        clean()
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
            clean()
            geoPlanaPoligonosTriangulo()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def geoPlanaPoligonosTriangulo():
    while True:
        clean()
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
            clean()
            geoPlanaPoligonosTrianguloPitágoras()

        # Formação de Triângulos
        elif escolha == "Formação de Triângulo":
            clean()
            formaçãoTriângulo(input("Lado 1 do Triângulo:"), input("Lado 2 do Triângulo:"), input("Lado 3 do Triângulo:"), True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def geoPlanaPoligonosTrianguloPitágoras():
    while True:
        clean()
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
            clean()
            pitagorasHipotenusa(input("Cateto:"), input("Cateto:"), True)
            voltar()

        # Teorema de Pitágoras para descobrir o Cateto
        elif escolha == "Calcular Cateto":
            clean()
            pitagorasCateto(input("Cateto:"), input("Hipotenusa:"), True)
            voltar()

        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()