from i_node import Inode
from datetime import date


def touch(entrada, lista_inodes, diretorioAtual):
    # Função que cria um arquivo 
    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')
    # nome nao tem extensao, vira .txt
    # print(diretorioAtual)
    lista_inodes.append(Inode(entrada, "eu", data_criacao_formatada)) # Cria o iNode e adiciona na lista de iNodes
    print(lista_inodes[len(lista_inodes)-1].data_de_criacao)
    for i, inode in enumerate(lista_inodes):
        # print(inode)
        if diretorioAtual.split("/",1) in inode.nome:
            # Adiciona um ponteiro para esse novo iNode, no diretório atual
            if len(lista_inodes[i].ponteiros_iNodes) == 1 and lista_inodes[i].ponteiros_iNodes[0] == 'vazio':
                lista_inodes[i].ponteiros_iNodes.pop(0)
            print(f'Adicionado o iNode {entrada}, no iNode {inode.nome}')
            lista_inodes[i].ponteiros_iNodes.append(entrada)
            print(f'Lista de ponteiros Inodes do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
    print(f'Nome do arquivo criado: {lista_inodes[len(lista_inodes)-1].nome}')
    # for pos in enumerate(lista_inodes):
    #     print(pos[1].nome)
    return lista_inodes