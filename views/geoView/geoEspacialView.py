from functions.functions import (
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from functions.geoF import (
    volumePrisma,
    volumeCubo,
    volumeParalelepipedo,
    volumeEsfera,
    volumeCilindro,
    volumeCone,
    volumeTroncoCone,
)

def geometriaEspacial():
    while True:
        clean()
        print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA ESPACIAL")
        print(YELLOW + "1) Volumes")
        print(RED + "0) Voltar" + RESET)
        print("")
        print("Qual ação deseja fazer?")
        escolha = get_keypress()

        # Prisma
        if escolha == "1":
            geometriaEspacialVolumes()
        
        elif escolha == "0":
            clean()
            break
        else:
            acaoInvalida()


def geometriaEspacialVolumes():
    while True:
            clean()
            print(GREEN + "TELA INICIAL -> GEOMETRIA -> GEOMETRIA ESPACIAL -> VOLUMES")
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
                volumePrisma(input("Quantidade de Lados da Base:"), input("Medida do Lado da Base:"), input("Altura do Prisma:"), True)
                voltar()

            # Cubo 
            elif escolha == "2":
                clean()
                volumeCubo(input("Medida da Aresta do Cubo:"), True)
                voltar()

            # Paralelepípedo 
            elif escolha == "3":
                clean()
                volumeParalelepipedo(input("Comprimento:"), input("Largura:"), input("Altura:"), True)
                voltar()

            # Esfera
            elif escolha == "4":
                clean()
                volumeEsfera(input("Raio:"), True)
                voltar()

            # Cilindro
            elif escolha == "5":
                clean()
                volumeCilindro(input("Raio da Base:"), input("Altura:"), True)
                voltar()

            # Cone
            elif escolha == "6":
                clean()
                volumeCone(input("Raio da Base:"), input("Altura:"), True)
                voltar()

            # Tronco do Cone
            elif escolha == "7":
                clean()
                volumeTroncoCone(input("Raio Maior:"), input("Raio Menor:"), input("Altura:"), True)
                voltar()
            
            elif escolha == "0":
                clean()
                break
            else:
                acaoInvalida()
