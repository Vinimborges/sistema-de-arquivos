def Ler_memoria():
    with open("Disco.txt", "r") as disco:
        memoria = disco.readlines()
        return memoria
