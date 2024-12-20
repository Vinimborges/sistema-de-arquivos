def rm(entrada, lista_inodes, lista_controle_blocos):
    for i,inode in enumerate(lista_inodes):
        if entrada == inode.nome:
            # Se o iNode existir, exclui ele da lista de iNodes
            for posicao, bloco in enumerate(inode.ponteiros_blocos):
                # Muda todos os blocos desse iNode de 1 para 0
                # Isso significa que os blocos agora estão livres para serem 
                # escritos
                
                # print(lista_controle_blocos[int(bloco)])
                lista_controle_blocos[int(bloco)] = "0"
                # print(lista_controle_blocos[int(bloco)])
            lista_inodes.pop(i)
        else:     
            for j, ponteiro in enumerate(inode.ponteiros_iNodes):
                # Percorre cada iNode, removendo o ponteiro para o 
                # iNode que foi excluido
                if entrada == ponteiro:
                    lista_inodes[i].ponteiros_iNodes.pop(j)
                    print(f'Ponteiro {ponteiro} removido do iNode {inode.nome}')
                    print(f'Nova lista de ponteiros do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
            if entrada in inode.nome:
                for pos in enumerate(lista_inodes):
                    print(pos[1].nome)
            
    
        
    return lista_inodes,lista_controle_blocos
    