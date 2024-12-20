def cat(entrada, diretorioAtual, lista_blocos, lista_inodes):
    controle = 0
    for Inode in lista_inodes:
        if (Inode.nome == diretorioAtual.split("/")[-1]):
            for idPonteiro in Inode.ponteiros_iNodes:
                for i, inode_acessado in enumerate(lista_inodes):
                    if idPonteiro == inode_acessado.id and entrada == inode_acessado.nome:
                        # for arquivo in lista_inodes:
                        #     if (arquivo.nome == conteudo):
                        for pega in inode_acessado.ponteiros_blocos:
                            print("".join(lista_blocos[pega]))
                            controle = 1
                            break
    if (controle == 1):
        return lista_blocos
    else:
        print("O arquivo não existe ou não está no diretório atual.")
        return lista_blocos

