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

    pitagorasHipotenusa,
    pitagorasCateto,

    formaçãoTriângulo,
)

def geometriaPlana():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA")
        print(YELLOW + "1) Polígonos")
        print("2) Áreas")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress() 

        # Áreas
        if escolha == "1":
            geoPlanaPoligonos()
        
        # Pitágoras
        elif escolha == "2":
            geoPlanaAreas()
        
        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geoPlanaAreas():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> ÁREAS")
        print(YELLOW + "1) Área de um Polígono Regular")
        print("2) Área do Cículo")
        print("3) Área do Quadrado")
        print("4) Área do Triângulo +")
        print("5) Área do Trapézio")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress() 

        # Polígono Regular Qualquer
        if escolha == "1":
            clean()
            areaPoliRegular(input("Quantidade de Lados do Polígono:"), input("Medida do Lado do Polígono:"), True)
            voltar()

        # Círculo
        elif escolha == "2":
            clean()
            areaCírculo(input("Raio do Círculo:"), True)
            voltar()

        # Quadrado
        elif escolha == "3":
            clean()
            areaQuadrado(input("Lado do Quadrado:"), True)
            voltar()

        # Triângulo
        elif escolha == "4":
            clean()
            print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> ÁREAS -> ÁREA TRIÂNGULO")
            print(YELLOW + "1)Base e Altura")
            print("2)Fórmula de Heron")
            print(RED + "0) Voltar" + RESET)
            print("")
            print("Qual ação deseja fazer?")
            escolhaTriangulo = get_keypress()

            if escolhaTriangulo == "1":  # Base e Altura
                clean()
                areaTriangulo(input("Base do triagulo:"), input("Altura do triagulo:"), True)
                voltar()

            elif escolhaTriangulo == "2":  # Fórmula de Heron
                clean()
                areaTrianguloHeron(input("Lado 1 do Triângulo:"), input("Lado 2 do Triângulo:"), input("Lado 3 do Triângulo:"), True)
                voltar()

            elif escolhaTriangulo == "0":
                clean()
                pass
            else:
                acaoInvalida()

        # Trapézio
        elif escolha == "5":
            clean()
            areaTrapezio(input("Base1 do Trapézio:"), input("Base2 do Trapézio:"), input("Altura do Trapézio:"), True)
            voltar()
        
        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()

def geoPlanaPoligonos():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> POLÍGONOS")
        print(YELLOW + "1) Triângulo+")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Triângulos
        if escolha == "1":
            clean()
            geoPlanaPoligonosTriangulo()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geoPlanaPoligonosTriangulo():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> POLÍGONOS -> TRIÂNGULO")
        print(YELLOW + "1) Teorema de Pitágoras+")
        print("2) Formação de Triângulos")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Teorema de Pitágoras
        if escolha == "1": 
            clean()
            geoPlanaPoligonosTrianguloPitágoras()

        # Formação de Triângulos
        elif escolha == "2":
            clean()
            formaçãoTriângulo(input("Lado 1 do Triângulo:"), input("Lado 2 do Triângulo:"), input("Lado 3 do Triângulo:"), True)
            voltar()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geoPlanaPoligonosTrianguloPitágoras():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> POLÍGONOS -> TRIÂNGULO -> TEOREMA DE PITÁGORAS")
        print(YELLOW + "1) Calcular Hipotenusa")
        print("2) Calcular Cateto")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Teorema de Pitágoras para descobrir a Hipotenusa
        if escolha == "1":
            clean()
            pitagorasHipotenusa(input("Cateto:"), input("Cateto:"), True)
            voltar()

        # Teorema de Pitágoras para descobrir o Cateto
        elif escolha == "2":
            clean()
            pitagorasCateto(input("Cateto:"), input("Hipotenusa:"), True)
            voltar()

        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()