from InquirerPy import prompt
from functions.functions import (
    clean, voltar, acao_invalida, 
)
from functions.geoFunctions.geoEspacial import (
    volume_prisma,
    volume_cubo,
    volume_paralelepipedo,
    volume_esfera,
    volume_cilindro,
    volume_cone,
    volume_tronco_cone,
)


def geometria_espacial():
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
            geometria_espacial_volumes()
        
        # Voltar
        elif escolha == "Voltar":
            clean()
            break
        else:
            acao_invalida()


def geometria_espacial_volumes():
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
                volume_prisma(input("Quantidade de Lados da Base:"), input("Medida do Lado da Base:"), input("Altura do Prisma:"), True)
                voltar()

            # Cubo 
            elif escolha == "Cubo":
                clean()
                volume_cubo(input("Medida da Aresta do Cubo:"), True)
                voltar()

            # Paralelepípedo 
            elif escolha == "Paralelepípedo":
                clean()
                volume_paralelepipedo(input("Comprimento:"), input("Largura:"), input("Altura:"), True)
                voltar()

            # Esfera
            elif escolha == "Esfera":
                clean()
                volume_esfera(input("Raio:"), True)
                voltar()

            # Cilindro
            elif escolha == "Cilindro":
                clean()
                volume_cilindro(input("Raio da Base:"), input("Altura:"), True)
                voltar()

            # Cone
            elif escolha == "Cone":
                clean()
                volume_cone(input("Raio da Base:"), input("Altura:"), True)
                voltar()

            # Tronco do Cone
            elif escolha == "Tronco de Cone":
                clean()
                volume_tronco_cone(input("Raio Maior:"), input("Raio Menor:"), input("Altura:"), True)
                voltar()
            
            # Voltar
            elif escolha == "Voltar":
                clean()
                break
            else:
                acao_invalida()