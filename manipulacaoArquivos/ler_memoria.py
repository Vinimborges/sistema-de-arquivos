def Ler_memoria():
    with open("disco.txt", "r") as disco:
        conteudo_disco = disco.readlines()
        lista_conteudo_disco = list(conteudo_disco)
        return lista_conteudo_disco