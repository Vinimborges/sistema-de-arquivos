def Ler_memoria():
    with open("disco.txt", "r") as disco:
        memoria = disco.readlines()
        return memoria
