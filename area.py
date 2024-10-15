import time, os  
from funcoes import(
inserirFLOAT, voltar,
areaCírculo,
areaQuadrado,
areaTrapezio,
areaTriangulo,
areaTrianguloHeron,
)

from funcoes import(
RESET,
RED,
GREEN,
YELLOW,
)

def area():
    while True:
        os.system("cls")
        print(YELLOW + "1) Área do Cículo")
        print("2) Área do Quadrado")
        print("3) Área do Triângulo")
        print("4) Área do Trapézio")
        print(RED + "0) Voltar" + RESET)
        escolha = input("Qual ação deseja fazer?:")

        # Círculo
        if escolha == "1":
            os.system("cls")
            circulo = areaCírculo(inserirFLOAT("Raio do Círculo em Metros:"))
            print(GREEN + "Área:",circulo,"m²" + RESET)
            print("")
            input(voltar())

        # Quadrado
        elif escolha == "2":
            os.system("cls")
            quadrado = areaQuadrado(inserirFLOAT("Lado do Quadrado em Metros:"))
            print(GREEN + "Área:",quadrado,"m²" + RESET)
            print("")
            input(voltar())

        # Triângulo
        elif escolha == "3":
            os.system("cls")
            print(YELLOW + "1)Base e Altura")
            print("2)Fórmula de Heron" + RESET)
            print("")
            print(voltar())
            escolhaTriangulo = input("Qual ação deseja fazer?:")


            if escolhaTriangulo == "1": #Base e Altura
                os.system("cls")
                triangulo = areaTriangulo(inserirFLOAT("Base do triagulo em Metros:"), inserirFLOAT("Altura do triagulo em Metros:"))
                print(GREEN + "Área:",triangulo,"m²" + RESET)
                print("")
                input(voltar())
            elif escolhaTriangulo == "2": #Fórmula de Heron
                os.system("cls")
                trianguloHeron = areaTrianguloHeron(inserirFLOAT("Lado 1 do Triângulo:"), inserirFLOAT("Lado 2 do Triângulo:"), inserirFLOAT("Lado 3 do Triângulo:"))
                print(GREEN + "Área:", trianguloHeron,"m²" + RESET)
                print("")
                input(voltar())
            else:
                pass
            
        # Trapézio
        elif escolha == "4":
            os.system("cls")
            trapezio = areaTrapezio(inserirFLOAT("Base1 do Trapézio em Metros:"), inserirFLOAT("Base2 do Trapézio em Metros"), inserirFLOAT("Altura do Trapézio em Metros:"))
            print(GREEN + "Área:",trapezio,"m²" + RESET)
            print("")
            input(voltar())

        # Sair
        elif escolha == "0":
            os.system("cls")
            break

        else:
            print(RED + "Favor selecionar uma ação válida." + RESET)
            time.sleep(1)