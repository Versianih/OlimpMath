from InquirerPy import prompt
from functions.tools import Tools
from functions.geoFunctions.geoEspacial import Geometria_Espacial


def geometria_espacial():
    while True:
        Tools.clean()
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
            geometria_espacial_volumes()
        
        # Voltar
        elif escolha == "Voltar":
            Tools.clean()
            break


def geometria_espacial_volumes():
    while True:
            Tools.clean()
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
                Tools.clean()
                Geometria_Espacial.Volume.volume_prisma(input("Quantidade de Lados da Base:"), input("Medida do Lado da Base:"), input("Altura do Prisma:"), True)
                Tools.voltar()

            # Cubo 
            elif escolha == "Cubo":
                Tools.clean()
                Geometria_Espacial.Volume.volume_cubo(input("Medida da Aresta do Cubo:"), True)
                Tools.voltar()

            # Paralelepípedo 
            elif escolha == "Paralelepípedo":
                Tools.clean()
                Geometria_Espacial.Volume.volume_paralelepipedo(input("Comprimento:"), input("Largura:"), input("Altura:"), True)
                Tools.voltar()

            # Esfera
            elif escolha == "Esfera":
                Tools.clean()
                Geometria_Espacial.Volume.volume_esfera(input("Raio:"), True)
                Tools.voltar()

            # Cilindro
            elif escolha == "Cilindro":
                Tools.clean()
                Geometria_Espacial.Volume.volume_cilindro(input("Raio da Base:"), input("Altura:"), True)
                Tools.voltar()

            # Cone
            elif escolha == "Cone":
                Tools.clean()
                Geometria_Espacial.Volume.volume_cone(input("Raio da Base:"), input("Altura:"), True)
                Tools.voltar()

            # Tronco do Cone
            elif escolha == "Tronco de Cone":
                Tools.clean()
                Geometria_Espacial.Volume.volume_tronco_cone(input("Raio Maior:"), input("Raio Menor:"), input("Altura:"), True)
                Tools.voltar()
            
            # Voltar
            elif escolha == "Voltar":
                Tools.clean()
                break