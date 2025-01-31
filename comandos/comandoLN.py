from i_node import Inode
from datetime import date
id_dirAtual = 0
id_dir = 0
id_diretorioAtual = 0

def ln(nomeLink, nomeInode, lista_inodes, diretorioAtual):
    # Função que cria um link para um inode

    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')
    
    for inode in lista_inodes:
        # Verifica se nome do link ja existe no diretório atual
        if diretorioAtual.split("/")[-1] in inode.nome:
                global id_diretorioAtual
                id_diretorioAtual = inode.id
                for i,ponteiro in enumerate(inode.ponteiros_iNodes):
                    for ind_inode, inode_acessado in enumerate(lista_inodes):
                        if ponteiro == inode_acessado.id and nomeLink == inode_acessado.nome:
                            print(f"Erro: Nome {nomeLink} já está sendo usado.")
                            return lista_inodes
                    
    # Cria um novo Inode para o diretório
    lista_inodes.append(Inode( lista_inodes[len(lista_inodes)-1].id + 1, nomeLink, "eu", data_criacao_formatada)) # Cria o iNode e adiciona na lista de iNodes
    
    lista_inodes[len(lista_inodes)-1].ponteiros_iNodes.append(nomeInode)
    id_dir = lista_inodes[len(lista_inodes)-1].id

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual.split("/")[-1] == inode.nome and inode.id == id_diretorioAtual:
            # Adiciona um ponteiro para esse novo iNode, no diretório atual
            lista_inodes[i].ponteiros_iNodes.append(id_dir)

            print(f"Link {nomeLink} adicionado ao diretório {diretorioAtual}.")
            break
    
    print(f"Link {nomeLink} criado com sucesso.")
    
    return lista_inodes
