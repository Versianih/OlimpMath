from InquirerPy import prompt
from functions.functions import (
    clean, get_keypress, voltar, acaoInvalida,
    RESET, RED, YELLOW, GREEN,    
)
from functions.geoFunctions.geoEspacial import (
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
        campos = [
            {
                "type": "list",
                "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA ESPACIAL",
                "choices": ["Volumes", "Voltar"],
            }
        ]
        escolha = prompt(campos)
        escolha = escolha.get(0)

        # Volumes
        if escolha == "Volumes":
            geometriaEspacialVolumes()
        
        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acaoInvalida()


def geometriaEspacialVolumes():
    while True:
            clean()
            campos = [
                {
                    "type": "list",
                    "message": "TELA INICIAL -> GEOMETRIA -> GEOMETRIA ESPACIAL -> VOLUMES",
                    "choices": ["Prisma Base n", "Cubo", "Paralelepípedo", "Esfera", "Cilindro", "Cone", "Tronco de Cone", "Voltar"],
                }
            ]
            escolha = prompt(campos)
            escolha = escolha.get(0)

            # Prisma
            if escolha == "Prisma Base n":
                clean()
                volumePrisma(input("Quantidade de Lados da Base:"), input("Medida do Lado da Base:"), input("Altura do Prisma:"), True)
                voltar()

            # Cubo 
            elif escolha == "Cubo":
                clean()
                volumeCubo(input("Medida da Aresta do Cubo:"), True)
                voltar()

            # Paralelepípedo 
            elif escolha == "Paralelepípedo":
                clean()
                volumeParalelepipedo(input("Comprimento:"), input("Largura:"), input("Altura:"), True)
                voltar()

            # Esfera
            elif escolha == "Esfera":
                clean()
                volumeEsfera(input("Raio:"), True)
                voltar()

            # Cilindro
            elif escolha == "Cilindro":
                clean()
                volumeCilindro(input("Raio da Base:"), input("Altura:"), True)
                voltar()

            # Cone
            elif escolha == "Cone":
                clean()
                volumeCone(input("Raio da Base:"), input("Altura:"), True)
                voltar()

            # Tronco do Cone
            elif escolha == "Tronco de Cone":
                clean()
                volumeTroncoCone(input("Raio Maior:"), input("Raio Menor:"), input("Altura:"), True)
                voltar()
            
            # Voltar
            elif escolha == "Voltar":
                clean()
                break
            else:
                acaoInvalida()