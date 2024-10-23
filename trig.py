import os  
from funcoes import(
    inserirFLOAT, voltar,acaoInvalida, resultado, get_keypress, clean,
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
    GREEN,
)

def trig():
    while True:
        clean()
        print(GREEN + "TRIGONOMETRIA PLANA")
        print(YELLOW + "1) Calcular Hipotenusa")
        print("2) Calcular Cateto Oposto")
        print("3) Calcular Cateto Adjacente")
        print("4) Calcular Ângulo")
        print(RED +"0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?:")
        escolha = get_keypress()

        if escolha == "1":
            hipotenusa()

        elif escolha == "2":
            oposto()
        
        elif escolha == "3":
            adjacente()

        elif escolha == "4":
            angulo()

        elif escolha == "0":
            os.system("cls")
            break

        else:
            acaoInvalida()

def hipotenusa():
    clean()
    print(YELLOW + "1)Calcular Hipotenusa com Cateto Oposto")
    print("2)Calcular Hipotensa com Cateto Adjacente" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?:")
    escolhaHipotensa = get_keypress()

    if escolhaHipotensa == "1":
        os.system("cls")
        HipotenusaOposto = HipotenusaComOposto(inserirFLOAT("Cateto Oposto:"), inserirFLOAT("Ângulo:"))
        resultado(HipotenusaOposto)
        voltar()

    elif escolhaHipotensa == "2":
        os.system("cls")
        HipotenusaAdjacente = HipotenusaComAdjacente(inserirFLOAT("Cateto Adjacente:"), inserirFLOAT("Ângulo:"))
        resultado(HipotenusaAdjacente)
        voltar()
        
    elif escolhaHipotensa == "0":
        clean()
        pass
    else:
        acaoInvalida()



def oposto():
    clean()
    print(YELLOW + "1)Calcular Cateto Oposto com Hipotenusa")
    print("2)Calcular Cateto Oposto com Cateto Adjacente" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?")
    escolhaOposto = get_keypress()
    
    if escolhaOposto == "1":
        os.system("cls")
        OpostoHipotenusa = OpostoComHipotenusa(inserirFLOAT("Hipotenusa:"), inserirFLOAT("Ângulo:"))
        resultado(OpostoHipotenusa)
        voltar()

    elif escolhaOposto == "2":
        os.system("cls")
        OpostoAdjacente = OpostoComAdjacente(inserirFLOAT("Cateto Adjacente:"), inserirFLOAT("Ângulo:"))
        resultado(OpostoAdjacente)
        voltar()
    
    elif escolhaOposto == "0":
        clean()
        pass

    else:
        acaoInvalida()

def adjacente():
    clean()
    print(YELLOW + "1)Calcular Cateto Adjacente com Hipotenusa")
    print("2)Calcular Cateto Adjacente com Cateto Oposto" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?")
    escolhaAdjacente = get_keypress()
    
    if escolhaAdjacente == "1":
        os.system("cls")
        AdjacenteHipotenusa = AdjacenteComHipotenusa(inserirFLOAT("Hipotenusa:"), inserirFLOAT("Ângulo:"))
        resultado(AdjacenteHipotenusa)
        voltar()

    elif escolhaAdjacente == "2":
        os.system("cls")
        AdjacenteOposto = AdjacenteComOposto(inserirFLOAT("Cateto Adjacente:"), inserirFLOAT("Ângulo:"))
        resultado(AdjacenteOposto)
        voltar()

    elif escolhaAdjacente == "0":
        clean()
        pass
    else:
        acaoInvalida()

def angulo():
    clean()
    print(YELLOW + "1)Calcular Ângulo com os Catetos")
    print("2)Calcular Ângulo com Cateto Oposto e Hipotenusa")
    print("3)Calcular Ângulo com Cateto Adjacente e Hipotenusa" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?")
    escolhaAngulo = get_keypress()

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
    
    elif escolhaAngulo == "0":
        clean()
        pass
    else:
        acaoInvalida()