from funcoes import (
    clean, get_keypress, voltar, acaoInvalida,
    
    # Geometria Plana
    areaPoliRegular,
    areaCírculo,
    areaQuadrado,
    areaTrapezio,
    areaTriangulo,
    areaTrianguloHeron,

    # Geometria Espacial
    volumePrisma,
    volumeCubo,
    volumeParalelepipedo,
    volumeEsfera,
    volumeCilindro,
    volumeCone,
    volumeTroncoCone,

    # Geometria Analítica
    distPontos,
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
        print("3) Geometria Analítica")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()
        
        # Geometria Plana
        if escolha == "1":
            geometriaPlana()

        # Geometria Espacial
        elif escolha == "2":
            geometriaEspacial()

        # Geometria Analítica
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

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geometriaEspacial():
    while True:
        clean()
        print(GREEN + "GEOMETRIA ESPACIAL")
        print(YELLOW + "1) Volume de um Prisma de Base 'n' lados")
        print("2) Volume do Cubo")
        print("3) Volume do Paralelepípedo")
        print("4) Volume da Esfera")
        print("5) Volume da Cilindro")
        print("6) Volume do Cone")
        print("7) Volume do Tronco de Cone")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Prisma
        if escolha == "1":
            clean()
            volumePrisma(input("Quantidade de Lados da Base:"), input("Medida do Lado da Base;"), input("Altura do Prisma:"))
            voltar()

        # Cubo 
        elif escolha == "2":
            clean()
            volumeCubo(input("Medida da Aresta do Cubo:"))
            voltar()

        # Paralelepípedo 
        elif escolha == "3":
            clean()
            volumeParalelepipedo(input("Comprimento:"), input("Largura:"), input("Altura:"))
            voltar()

        # Esfera
        elif escolha == "4":
            clean()
            volumeEsfera(input("Raio:"))
            voltar()

        # Cilindro
        elif escolha == "5":
            clean()
            volumeCilindro(input("Raio da Base:"), input("Altura:"))
            voltar()

        # Cone
        elif escolha == "6":
            clean()
            volumeCone(input("Raio da Base:"), input("Altura:"))
            voltar()

        # Tronco do Cone
        elif escolha == "7":
            clean()
            volumeTroncoCone(input("Raio Maior:"), input("Raio Menor:"), input("Altura:"))
            voltar()
        
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geometriaAnalítica():
    while True:
        clean()
        print(GREEN + "GEOMETRIA ANALÍTICA")
        print(YELLOW + "1) Distância entre dois pontos")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        if escolha == "1":
            clean()
            distPontos(input("Xa:"), input("Ya:"), input("Xb:"), input("Yb:"))
            voltar()

        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()