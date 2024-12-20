def cat(entrada, diretorioAtual, lista_blocos, lista_inodes):
    controle = 0
    for Inode in lista_inodes:
        if (Inode.nome == diretorioAtual):
            for conteudo in Inode.ponteiros_iNodes:
                if (conteudo == entrada):
                    for arquivo in lista_inodes:
                        if (arquivo.nome == conteudo):
                            for pega in arquivo.ponteiros_blocos:
                                print("".join(lista_blocos[pega]))
                                controle = 1
    if (controle == 1):
        return lista_blocos
    else:
        print("O arquivo não existe ou não está no diretório atual.")
        return lista_blocos

