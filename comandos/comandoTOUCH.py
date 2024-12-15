from i_node import Inode

def touch(entrada, lista_inodes):
    # nome nao tem extensao, vira .txt
    lista_inodes.append(Inode(entrada, "eu"))
    print(f'Nome do arquivo criado: {lista_inodes[len(lista_inodes)-1].nome}')
    for pos in enumerate(lista_inodes):
        print(pos[1].nome)
    return lista_inodes