def Controle_blocos(lista_conteudo_disco):
    lista_controle_blocos = []
    blocos = []
    for i in range(15):
        blocos.append(lista_conteudo_disco[i])
        for j in range(len(blocos[i])-1):
            if blocos[i][j] == "0" or blocos[i][j] == "1":
                lista_controle_blocos.append(blocos[i][j])
    return lista_controle_blocos