from functions.functions import (
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from functions.geoF import (
    areaPoliRegular,
    areaCírculo,
    areaQuadrado,
    areaTrapezio,
    areaTriangulo,
    areaTrianguloHeron,

    pitagorasHipotenusa,
    pitagorasCateto,

)

def geometriaPlana():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA")
        print(YELLOW + "1) Áreas")
        print("2) Teorema de Pitágoras")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress() 

        # Áreas
        if escolha == "1":
            geoPlanaAreas()
        
        # Pitágoras
        elif escolha == "2":
            geoPlanaPitágoras()
        
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
            areaCírculo(input("Raio do Círculo em Metros:"), True)
            voltar()

        # Quadrado
        elif escolha == "3":
            clean()
            areaQuadrado(input("Lado do Quadrado em Metros:"), True)
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
                areaTriangulo(input("Base do triagulo em Metros:"), input("Altura do triagulo em Metros:"), True)
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
            areaTrapezio(input("Base1 do Trapézio em Metros:"), input("Base2 do Trapézio em Metros"), input("Altura do Trapézio em Metros:"), True)
            voltar()
        
        # Sair
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geoPlanaPitágoras():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA PLANA -> TEOREMA DE PITÁGORAS")
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