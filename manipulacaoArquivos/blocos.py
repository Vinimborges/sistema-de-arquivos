def Blocos(lista_conteudo_disco):
    lista_blocos = []
    for i in range(5536, 65536):
        print(f'Leu o {i}')
        lista_blocos.append(lista_conteudo_disco[i])

    return lista_blocos