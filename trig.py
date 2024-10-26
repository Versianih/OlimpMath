from funcoes import(
    voltar, acaoInvalida, resultado, get_keypress, clean,
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
        print(YELLOW + "1) Calcular Hipotenusa +")
        print("2) Calcular Cateto Oposto +")
        print("3) Calcular Cateto Adjacente +")
        print("4) Calcular Ângulo +")
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
            clean()
            break

        else:
            acaoInvalida()

def hipotenusa():
    clean()
    print(GREEN + "HIPOTENUSA")
    print(YELLOW + "1)Calcular Hipotenusa com Cateto Oposto")
    print("2)Calcular Hipotensa com Cateto Adjacente" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?:")
    escolhaHipotensa = get_keypress()

    if escolhaHipotensa == "1":
        clean()
        HipotenusaComOposto(input("Cateto Oposto:"), input("Ângulo:"))
        voltar()

    elif escolhaHipotensa == "2":
        clean()
        HipotenusaComAdjacente(input("Cateto Adjacente:"), input("Ângulo:"))
        voltar()
        
    elif escolhaHipotensa == "0":
        clean()
        pass
    else:
        acaoInvalida()



def oposto():
    clean()
    print(GREEN + "CATETO OPOSTO")
    print(YELLOW + "1)Calcular Cateto Oposto com Hipotenusa")
    print("2)Calcular Cateto Oposto com Cateto Adjacente" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?")
    escolhaOposto = get_keypress()
    
    if escolhaOposto == "1":
        clean()
        OpostoComHipotenusa(input("Hipotenusa:"), input("Ângulo:"))
        voltar()

    elif escolhaOposto == "2":
        clean()
        OpostoComAdjacente(input("Cateto Adjacente:"), input("Ângulo:"))
        voltar()
    
    elif escolhaOposto == "0":
        clean()
        pass

    else:
        acaoInvalida()

def adjacente():
    clean()
    print(GREEN + "CATETO ADJACENTE")
    print(YELLOW + "1)Calcular Cateto Adjacente com Hipotenusa")
    print("2)Calcular Cateto Adjacente com Cateto Oposto" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?")
    escolhaAdjacente = get_keypress()
    
    if escolhaAdjacente == "1":
        clean()
        AdjacenteComHipotenusa(input("Hipotenusa:"), input("Ângulo:"))
        voltar()

    elif escolhaAdjacente == "2":
        clean()
        AdjacenteComOposto(input("Cateto Adjacente:"), input("Ângulo:"))
        voltar()

    elif escolhaAdjacente == "0":
        clean()
        pass
    else:
        acaoInvalida()

def angulo():
    clean()
    print(GREEN + "ÂNGULO")
    print(YELLOW + "1)Calcular Ângulo com os Catetos")
    print("2)Calcular Ângulo com Cateto Oposto e Hipotenusa")
    print("3)Calcular Ângulo com Cateto Adjacente e Hipotenusa" + RESET)
    print(RED + "0) Sair" + RESET)
    print("")
    print("Qual ação deseja fazer?")
    escolhaAngulo = get_keypress()

    if escolhaAngulo == "1":
        clean()
        AnguloComCOCA(input("Cateto Oposto:"), input("Cateto Adjacente:"))
        voltar()

    elif escolhaAngulo == "2":
        clean()
        AnguloComCOH(input("Cateto Oposto:"), input("Hipotenusa:"))
        voltar()

    elif escolhaAngulo == "3":
        clean()
        AnguloComCAH(input("Cateto Adjacente:"), input("Hipotenusa"))
        voltar()
    
    elif escolhaAngulo == "0":
        clean()
        pass
    else:
        acaoInvalida()