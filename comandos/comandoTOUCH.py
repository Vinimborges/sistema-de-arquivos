from i_node import Inode

def touch(entrada, lista_inodes, diretorioAtual):
    # nome nao tem extensao, vira .txt
    # print(diretorioAtual)
    lista_inodes.append(Inode(entrada, "eu"))
    for i, inode in enumerate(lista_inodes):
        # print(inode)
        if diretorioAtual in inode.nome:
            print(f'Adicionado o iNode {entrada}, no iNode {inode.nome}')
            lista_inodes[i].ponteiros_iNodes.append(entrada)
            print(f'Lista de ponteiros Inodes do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
    print(f'Nome do arquivo criado: {lista_inodes[len(lista_inodes)-1].nome}')
    # for pos in enumerate(lista_inodes):
    #     print(pos[1].nome)
    return lista_inodes