from funcoes import (
    clean, get_keypress, voltar, acaoInvalida,
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
        print("4) Área do Triângulo +")
        print("5) Área do Trapézio")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress() 

        # Polígono Regular Qualquer
        if escolha == "1":
            clean()
            areaPoliRegular(input("Quantidade de Lados do Polígono:"), input("Medida do Lado do Polígono:"))
            voltar()

        # Círculo
        elif escolha == "2":
            clean()
            areaCírculo(input("Raio do Círculo em Metros:"))
            voltar()

        # Quadrado
        elif escolha == "3":
            clean()
            areaQuadrado(input("Lado do Quadrado em Metros:"))
            voltar()

        # Triângulo
        elif escolha == "4":
            clean()
            print(GREEN + "Área Triângulo")
            print(YELLOW + "1)Base e Altura")
            print("2)Fórmula de Heron")
            print(RED + "0) Voltar" + RESET)
            print("")
            print("Qual ação deseja fazer?")
            escolhaTriangulo = get_keypress()

            if escolhaTriangulo == "1":  # Base e Altura
                clean()
                areaTriangulo(input("Base do triagulo em Metros:"), input("Altura do triagulo em Metros:"))
                voltar()

            elif escolhaTriangulo == "2":  # Fórmula de Heron
                clean()
                areaTrianguloHeron(input("Lado 1 do Triângulo:"), input("Lado 2 do Triângulo:"), input("Lado 3 do Triângulo:"))
                voltar()

            elif escolhaTriangulo == "0":
                clean()
                break
            else:
                acaoInvalida()

        # Trapézio
        elif escolha == "5":
            clean()
            areaTrapezio(input("Base1 do Trapézio em Metros:"), input("Base2 do Trapézio em Metros"), input("Altura do Trapézio em Metros:"))
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