from i_node import Inode
from datetime import date
id_dirAtual = 0
def ln(nomeLink, nomeInode, lista_inodes, diretorioAtual):
    # Função que cria um link para um inode

    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')

    # Verifica se nome do link ja existe no diretório atual
    for inode in lista_inodes:
        if inode.nome == diretorioAtual:
            global id_dirAtual
            id_dirAtual = inode.id
            for ind_pont , pont in enumerate(inode.ponteiros_iNodes):
                for ind_inode, inode_acessado in enumerate(lista_inodes):
                    if pont == inode_acessado.id and nomeLink == inode_acessado.nome:
                        print(f"Erro: Nome {nomeLink} já está sendo usado.")
                        return lista_inodes
                    
    # Cria um novo Inode para o diretório
    lista_inodes.append(Inode( lista_inodes[len(lista_inodes)-1].id + 1, nomeLink, "eu", data_criacao_formatada)) # Cria o iNode e adiciona na lista de iNodes
    lista_inodes[len(lista_inodes)-1].ponteiros_iNodes.append(nomeInode)

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual == inode.nome and inode.id == id_dirAtual:
            # Adiciona um ponteiro para esse novo iNode, no diretório atual
            lista_inodes[i].ponteiros_iNodes.append(lista_inodes[len(lista_inodes)-1].id)

            print(f"Link {nomeLink} adicionado ao diretório {diretorioAtual}.")
            break
    
    print(f"Link {nomeLink} criado com sucesso.")
    
    return lista_inodes
