import os
from funcoes import (
    clean, get_keypress, inserirFLOAT, inserirINT, voltar, acaoInvalida, resultado, ERROR,
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
    GREEN,
)


def geometria():
    while True:
        clean()
        print(GREEN + "GEOMETRIA")
        print(YELLOW + "1) Geometria Plana")
        print("2) Geometria Espacial")
        print("3) Geometria Analítica(Não Funcional)")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()
        
        if escolha == "1":
            geometriaPlana()

        elif escolha == "2":
            geometriaEspacial()

        elif escolha == "3":
            geometriaAnalítica()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geometriaPlana():
    while True:
        clean()
        print(GREEN + "GEOMETRIA PLANA")
        print(YELLOW + "1) Área de um Polígono Regular")
        print("2) Área do Cículo")
        print("3) Área do Quadrado")
        print("4) Área do Triângulo")
        print("5) Área do Trapézio")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress() 

        if escolha == "1":
            clean()
            poligono = areaPoliRegular(inserirINT("Quantidade de Lados do Polígono:"), inserirFLOAT("Medida do Lado do Polígono:"))
            if poligono == "erro":
                ERROR("Verifique se a quantidade de lados permite um Polígono")
            else:
                resultado(poligono)
            voltar()

        # Círculo
        elif escolha == "2":
            clean()
            circulo = areaCírculo(inserirFLOAT("Raio do Círculo em Metros:"))
            resultado(circulo)
            voltar()

        # Quadrado
        elif escolha == "3":
            clean()
            quadrado = areaQuadrado(inserirFLOAT("Lado do Quadrado em Metros:"))
            resultado(quadrado)
            voltar()

        # Triângulo
        elif escolha == "4":
            clean()
            print(YELLOW + "1)Base e Altura")
            print("2)Fórmula de Heron")
            print(RED + "0) Voltar" + RESET)
            print("")
            print("Qual ação deseja fazer?")
            escolhaTriangulo = get_keypress()

            if escolhaTriangulo == "1":  # Base e Altura
                clean()

                triangulo = areaTriangulo(inserirFLOAT("Base do triagulo em Metros:"), inserirFLOAT("Altura do triagulo em Metros:"))
                resultado(triangulo)
                voltar()

            elif escolhaTriangulo == "2":  # Fórmula de Heron
                clean()

                trianguloHeron = areaTrianguloHeron(inserirFLOAT("Lado 1 do Triângulo:"), inserirFLOAT("Lado 2 do Triângulo:"), inserirFLOAT("Lado 3 do Triângulo:"))
                resultado(trianguloHeron)
                voltar()

            elif escolhaTriangulo == "0":
                clean()

                break
            else:
                acaoInvalida()

        # Trapézio
        elif escolha == "5":
            clean()
            trapezio = areaTrapezio(inserirFLOAT("Base1 do Trapézio em Metros:"), inserirFLOAT("Base2 do Trapézio em Metros"), inserirFLOAT("Altura do Trapézio em Metros:"))
            resultado(trapezio)
            voltar()

        # Sair
        elif escolha == "0":
            clean()
            break

        else:
            acaoInvalida()


def geometriaEspacial():
    while True:
        clean()
        print(GREEN + "GEOMETRIA ESPACIAL")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        if escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geometriaAnalítica():
    while True:
        clean()
        print(GREEN + "GEOMETRIA ANALÍTICA")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        if escolha == "0":
            clean()
            break
        else:
            acaoInvalida()