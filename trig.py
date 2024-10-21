import os  
from funcoes import(
    inserirFLOAT, voltar,acaoInvalida, resultado,
    HipotenusaComOposto,
    HipotenusaComAdjacente,
    OpostoComHipotenusa,
    OpostoComAdjacente,
    AdjacenteComHipotenusa,
    AdjacenteComOposto,
    AnguloComCOCA,
    AnguloComCOH,
    AnguloComCAH,
)

from funcoes import(
    RESET,
    RED,
    YELLOW,
)

def trig():
    while True:
        os.system("cls")
        print(YELLOW + "1) Calcular Hipotenusa")
        print("2) Calcular Cateto Oposto")
        print("3) Calcular Cateto Adjacente")
        print("4) Calcular Ângulo")
        print(RED +"0) Voltar" + RESET)
        escolha = input("Qual ação deseja fazer?:")


        if escolha == "1":
            os.system("cls")
            print(YELLOW + "1)Calcular Hipotenusa com Cateto Oposto")
            print("2)Calcular Hipotensa com Cateto Adjacente" + RESET)
            print("")
            print(RED + "Voltar(Enter)" + RESET)
            escolhaHipotensa = input("Qual ação deseja fazer?:")
        
            if escolhaHipotensa == "1":
                os.system("cls")
                HipotenusaOposto = HipotenusaComOposto(inserirFLOAT("Cateto Oposto:"), inserirFLOAT("Ângulo:"))
                resultado(HipotenusaOposto)
                voltar()

            if escolhaHipotensa == "2":
                os.system("cls")
                HipotenusaAdjacente = HipotenusaComAdjacente(inserirFLOAT("Cateto Adjacente:"), inserirFLOAT("Ângulo:"))
                resultado(HipotenusaAdjacente)
                voltar()
                
            else:
                pass
        

        elif escolha == "2":
            os.system("cls")
            print(YELLOW + "1)Calcular Cateto Oposto com Hipotenusa")
            print("2)Calcular Cateto Oposto com Cateto Adjacente" + RESET)
            print("")
            print(RED + "Voltar(Enter)" + RESET)
            escolhaOposto = input("Qual ação deseja fazer?:")
            
            if escolhaOposto == "1":
                os.system("cls")
                OpostoHipotenusa = OpostoComHipotenusa(inserirFLOAT("Hipotenusa:"), inserirFLOAT("Ângulo:"))
                resultado(OpostoHipotenusa)
                voltar()

            if escolhaOposto == "2":
                os.system("cls")
                OpostoAdjacente = OpostoComAdjacente(inserirFLOAT("Cateto Adjacente:"), inserirFLOAT("Ângulo:"))
                resultado(OpostoAdjacente)
                voltar()
            else:
                pass

        
        elif escolha == "3":
            os.system("cls")
            print(YELLOW + "1)Calcular Cateto Adjacente com Hipotenusa")
            print("2)Calcular Cateto Adjacente com Cateto Oposto" + RESET)
            print("")
            print(RED + "Voltar(Enter)" + RESET)
            escolhaAdjacente = input("Qual ação deseja fazer?:")
            
            if escolhaAdjacente == "1":
                os.system("cls")
                AdjacenteHipotenusa = AdjacenteComHipotenusa(inserirFLOAT("Hipotenusa:"), inserirFLOAT("Ângulo:"))
                resultado(AdjacenteHipotenusa)
                voltar()

            if escolhaAdjacente == "2":
                os.system("cls")
                AdjacenteOposto = AdjacenteComOposto(inserirFLOAT("Cateto Adjacente:"), inserirFLOAT("Ângulo:"))
                resultado(AdjacenteOposto)
                voltar()

            else:
                pass


        elif escolha == "4":
            os.system("cls")
            print(YELLOW + "1)Calcular Ângulo com os Catetos")
            print("2)Calcular Ângulo com Cateto Oposto e Hipotenusa")
            print("3)Calcular Ângulo com Cateto Adjacente e Hipotenusa" + RESET)
            print("")
            print(RED + "Voltar(Enter)" + RESET)
            escolhaAngulo = input("Qual ação deseja fazer?:")

            if escolhaAngulo == "1":
                os.system("cls")
                AnguloCOCA = AnguloComCOCA(inserirFLOAT("Cateto Oposto:"), inserirFLOAT("Cateto Adjacente:"))
                resultado(AnguloCOCA)
                voltar()

            elif escolhaAngulo == "2":
                os.system("cls")
                AnguloCOH = AnguloComCOH(inserirFLOAT("Cateto Oposto:"), inserirFLOAT("Hipotenusa:"))
                resultado(AnguloCOH)
                voltar()

            elif escolhaAngulo == "3":
                os.system("cls")
                AnguloCAH = AnguloComCAH(inserirFLOAT("Cateto Adjacente:"), inserirFLOAT("Hipotenusa"))
                resultado(AnguloCAH)
                voltar()
            else:
                pass
        

        elif escolha == "0":
            os.system("cls")
            break

        else:
            acaoInvalida()