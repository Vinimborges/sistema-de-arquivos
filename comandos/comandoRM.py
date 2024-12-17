def rm(entrada, lista_inodes):
    for i,inode in enumerate(lista_inodes):
        for j, ponteiro in enumerate(inode.ponteiros_iNodes):
            if entrada == ponteiro:
                lista_inodes[i].ponteiros_iNodes.pop(j)
                print(f'Ponteiro {ponteiro} removido do iNode {inode.nome}')
                print(f'Nova lista de ponteiros do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
        if entrada in inode.nome:
            lista_inodes.pop(i)
            for pos in enumerate(lista_inodes):
                print(pos[1].nome)
    
        
    return lista_inodes
    