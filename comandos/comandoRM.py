# funcao para retornar o id do arquivo a ser deletado
def encontra_arquivo(entrada,diretorioAtual, lista_inodes, lista_controle_blocos):
    id = None
    idPai = None
    caminho = diretorioAtual.split("/")
    
    for posicao in range(len(caminho)):
        for i,inode in enumerate(lista_inodes):
            if inode.nome == caminho[posicao]:
                # print(posicao,"..",inode.nome)
                for filhos in inode.ponteiros_iNodes:
                    for j,inodeP in enumerate(lista_inodes):
                        if posicao == len(caminho) - 1:
                            if inodeP.id == filhos and inodeP.nome == entrada:
                                # print(inodeP.id,"--",inodeP.nome)
                                id = inodeP.id 
                                idPai = inode.id
    # print("id:",id)
    # print("idPAI:",idPai)
    return id, idPai

def rm(entrada, diretorioAtual, lista_inodes, lista_controle_blocos):
    id, idPai= encontra_arquivo(entrada, diretorioAtual, lista_inodes, lista_controle_blocos)

    if id == None:
        print("Arquivo não está no diretório")

    else:
        for i,inode in enumerate(lista_inodes):
            if inode.id == idPai:
                inode.ponteiros_iNodes.remove(id)
                print(inode.ponteiros_iNodes)

    # for i,inode in enumerate(lista_inodes):
    #     if entrada == inode.nome and len(inode.ponteiros_iNodes) == 0:
    #         id_inode = inode.id
    #         # Se o iNode existir, exclui ele da lista de iNodes
    #         for posicao, bloco in enumerate(inode.ponteiros_blocos):
    #             # Muda todos os blocos desse iNode de 1 para 0
    #             # Isso significa que os blocos agora estão livres para serem 
    #             # escritos
                
    #             # print(lista_controle_blocos[int(bloco)])
    #             lista_controle_blocos[int(bloco)] = "0"
    #             # print(lista_controle_blocos[int(bloco)])
    #         lista_inodes.pop(i)         
    #     else:     
    #         for j, ponteiro in enumerate(inode.ponteiros_iNodes):
    #             # Percorre cada iNode, removendo o ponteiro para o 
    #             # iNode que foi excluido
    #             if id_inode == ponteiro:
    #                 if len(lista_inodes[i].ponteiros_iNodes) == 1:
    #                     lista_inodes[i].ponteiros_iNodes.append('vazio')
    #                     lista_inodes[i].ponteiros_iNodes.pop(0)
    #                     print(f'Ponteiro {ponteiro} removido do iNode {inode.nome}')
    #                     print(f'Nova lista de ponteiros do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
    #                 else:
    #                     lista_inodes[i].ponteiros_iNodes.pop(j)
    #                     print(f'Ponteiro {ponteiro} removido do iNode {inode.nome}')
    #                     print(f'Nova lista de ponteiros do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
                    
    #                 # print(f'Ponteiro {ponteiro} removido do iNode {inode.nome}')
    #                 # print(f'Nova lista de ponteiros do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
    #         if entrada in inode.nome:
    #             for pos in enumerate(lista_inodes):
    #                 print(pos[1].nome)
            
    
        
    return lista_inodes,lista_controle_blocos
    