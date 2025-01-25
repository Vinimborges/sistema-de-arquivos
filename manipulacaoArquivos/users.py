def Users(lista_conteudo_disco):
    lista_users = []
    for i in range(15,100):
        if lista_conteudo_disco[i][0] != '\x00':
            sep = lista_conteudo_disco[i].split("=")
            for j in range(len(sep)):
                if sep[j][0] != '\x00':    
                    lista_users.append(dict(user=sep[j].split(",")[0], password=sep[j].split(",")[1]))
                    print(lista_users)
    return lista_users