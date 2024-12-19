

def cat(entrada, diretorioAtual, lista_blocos, lista_inodes):
    print(diretorioAtual)
    for Inode in lista_inodes:
        if (Inode.nome == diretorioAtual):
            for arq in Inode.ponteiros_iNodes:
                if (arq == entrada):
                    for teste in lista_inodes:
                        if (teste.nome == arq):
                            for pega in teste.ponteiros_blocos:
                                print("".join(lista_blocos[pega]))

    return lista_blocos

