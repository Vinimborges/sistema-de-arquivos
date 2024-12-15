def rm(entrada, lista_inodes):
    for i,inode in enumerate(lista_inodes):
        if entrada in inode.nome:
            lista_inodes.pop(i)
            for pos in enumerate(lista_inodes):
                print(pos[1].nome)
        
    return lista_inodes
    