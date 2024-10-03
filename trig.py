import time, os  
from funcoes import(
inserir, voltar,
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
GREEN,
YELLOW,
)


while True:
    os.system("cls")
    print(YELLOW + "1)Calcular Hipotenusa")
    print("2)Calcular Cateto Oposto")
    print("3)Calcular Cateto Adjacente")
    print("4)Calcular Ângulo")
    print(RED +"0)Sair" + RESET)
    escolha = input("Qual ação deseja fazer?:")


    if escolha == "1":
        os.system("cls")
        print(YELLOW + "1)Calcular Hipotenusa com Cateto Oposto")
        print("2)Calcular Hipotensa com Cateto Adjacente" + RESET)
        print("")
        print(voltar())
        escolhaHipotensa = input("Qual ação deseja fazer?:")
       
        if escolhaHipotensa == "1":
            os.system("cls")
            HipotenusaOposto = HipotenusaComOposto(inserir("Cateto Oposto:"), inserir("Ângulo:"))
            print(GREEN + "Hipotenusa:",HipotenusaOposto,"" + RESET)
            print("")
            input(voltar())

        if escolhaHipotensa == "2":
            os.system("cls")
            HipotenusaAdjacente = HipotenusaComAdjacente(inserir("Cateto Adjacente:"), inserir("Ângulo:"))
            print(GREEN + "Hipotenusa:",HipotenusaAdjacente,"" + RESET)
            print("")
            input(voltar())
            
        else:
            pass
    

    elif escolha == "2":
        os.system("cls")
        print(YELLOW + "1)Calcular Cateto Oposto com Hipotenusa")
        print("2)Calcular Cateto Oposto com Cateto Adjacente" + RESET)
        print("")
        print(voltar())
        escolhaOposto = input("Qual ação deseja fazer?:")
        
        if escolhaOposto == "1":
            os.system("cls")
            OpostoHipotenusa = OpostoComHipotenusa(inserir("Hipotenusa:"), inserir("Ângulo:"))
            print(GREEN + "Cateto Oposto:",OpostoHipotenusa,"" + RESET)
            print("")
            input(voltar())

        if escolhaOposto == "2":
            os.system("cls")
            OpostoAdjacente = OpostoComAdjacente(inserir("Cateto Adjacente:"), inserir("Ângulo:"))
            print(GREEN + "Cateto Oposto:",OpostoAdjacente,"" + RESET)
            print("")
            input(voltar())
        else:
            pass

    
    elif escolha == "3":
        os.system("cls")
        print(YELLOW + "1)Calcular Cateto Adjacente com Hipotenusa")
        print("2)Calcular Cateto Adjacente com Cateto Oposto" + RESET)
        print("")
        print(voltar())
        escolhaAdjacente = input("Qual ação deseja fazer?:")
        
        if escolhaAdjacente == "1":
            os.system("cls")
            AdjacenteHipotenusa = AdjacenteComHipotenusa(inserir("Hipotenusa:"), inserir("Ângulo:"))
            print(GREEN + "Cateto Oposto:",AdjacenteHipotenusa,"" + RESET)
            print("")
            input(voltar())

        if escolhaAdjacente == "2":
            os.system("cls")
            AdjacenteOposto = AdjacenteComOposto(inserir("Cateto Adjacente:"), inserir("Ângulo:"))
            print(GREEN + "Cateto Oposto:",AdjacenteOposto,"" + RESET)
            print("")
            input(voltar())

        else:
            pass


    elif escolha == "4":
        os.system("cls")
        print(YELLOW + "1)Calcular Ângulo com os Catetos")
        print("2)Calcular Ângulo com Cateto Oposto e Hipotenusa")
        print("3)Calcular Ângulo com Cateto Adjacente e Hipotenusa" + RESET)
        print("")
        print(voltar())
        escolhaAngulo = input("Qual ação deseja fazer?:")

        if escolhaAngulo == "1":
            os.system("cls")
            AnguloCOCA = AnguloComCOCA(inserir("Cateto Oposto:"), inserir("Cateto Adjacente:"))
            print(GREEN + "Ângulo:",AnguloCOCA,"" + RESET)
            print("")
            input(voltar())

        elif escolhaAngulo == "2":
            os.system("cls")
            AnguloCOH = AnguloComCOH(inserir("Cateto Oposto:"), inserir("Hipotenusa:"))
            print (GREEN + "Ângulo",AnguloCOH,"" + RESET)
            print("")
            input(voltar())

        elif escolhaAngulo == "3":
            os.system("cls")
            AnguloCAH = AnguloComCAH(inserir("Cateto Adjacente:"), inserir("Hipotenusa"))
            print(GREEN + "Ângulo",AnguloCAH,"" + RESET)
            print("")
            input(voltar())
        else:
            pass
    

    elif escolha == "0":
        os.system("cls")
        break

    else:
        print(RED + "Favor selecionar uma ação válida." + RESET)
        time.sleep(1)