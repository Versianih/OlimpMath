import os
from funcoes import (
    inserirFLOAT, inserirINT, voltar, acaoInvalida, resultado,
    areaPoliRegular,
    areaCírculo,
    areaQuadrado,
    areaTrapezio,
    areaTriangulo,
    areaTrianguloHeron,
)

from funcoes import (
    RESET,
    RED,
    YELLOW,
)


def geometria():
    while True:
        os.system("cls")
        print(YELLOW + "1) Geometria Plana")
        print("2) Geometria Espacial")
        print("3) Geometria Analítica(Não Funcional)")
        print(RED + "0) Voltar" + RESET)
        escolha = input("Qual ação deseja fazer?:")
        
        if escolha == "1":
            geometriaPlana()

        elif escolha == "2":
            geometriaPlana()

        elif escolha == "3":
            geometriaPlana()

        elif escolha == "0":
            os.system("cls")
            break
        else:
            acaoInvalida()


def geometriaPlana():
    while True:
        os.system("cls")
        print(YELLOW + "1) Área de um Polígono Regular")
        print("2) Área do Cículo")
        print("3) Área do Quadrado")
        print("4) Área do Triângulo")
        print("5) Área do Trapézio")
        print(RED + "0) Voltar" + RESET)
        escolha = input("Qual ação deseja fazer?:")

        if escolha == "1":
            os.system("cls")
            poligono = areaPoliRegular(inserirINT("Quantidade de Lados do Polígono:"), inserirFLOAT("Medida do Lado do Polígono:"))
            resultado(poligono)
            voltar()

        # Círculo
        elif escolha == "2":
            os.system("cls")
            circulo = areaCírculo(inserirFLOAT("Raio do Círculo em Metros:"))
            resultado(circulo)
            voltar()

        # Quadrado
        elif escolha == "3":
            os.system("cls")
            quadrado = areaQuadrado(inserirFLOAT("Lado do Quadrado em Metros:"))
            resultado(quadrado)
            voltar()

        # Triângulo
        elif escolha == "4":
            os.system("cls")
            print(YELLOW + "1)Base e Altura")
            print("2)Fórmula de Heron")
            print(RED + "0) Voltar" + RESET)
            print("")
            escolhaTriangulo = input("Qual ação deseja fazer?:")

            if escolhaTriangulo == "1":  # Base e Altura
                os.system("cls")
                triangulo = areaTriangulo(inserirFLOAT("Base do triagulo em Metros:"), inserirFLOAT("Altura do triagulo em Metros:"))
                resultado(triangulo)
                voltar()

            elif escolhaTriangulo == "2":  # Fórmula de Heron
                os.system("cls")
                trianguloHeron = areaTrianguloHeron(inserirFLOAT("Lado 1 do Triângulo:"), inserirFLOAT("Lado 2 do Triângulo:"), inserirFLOAT("Lado 3 do Triângulo:"))
                resultado(trianguloHeron)
                voltar()

            elif escolhaTriangulo == "0":
                os.system("cls")
                break
            else:
                acaoInvalida()

        # Trapézio
        elif escolha == "5":
            os.system("cls")
            trapezio = areaTrapezio(inserirFLOAT("Base1 do Trapézio em Metros:"), inserirFLOAT("Base2 do Trapézio em Metros"), inserirFLOAT("Altura do Trapézio em Metros:"))
            resultado(trapezio)
            voltar()

        # Sair
        elif escolha == "0":
            os.system("cls")
            break

        else:
            acaoInvalida()


def geometriaEspacial():
    while True:
        break


def geometriaAnalítica():
    while True:
        break