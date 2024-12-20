from i_node import Inode
from datetime import date

def ln(nomeLink, nomeInode, lista_inodes, diretorioAtual):
    # Função que cria um diretório

    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')

    # Verifica se nome do link ja existe no diretório atual
    for inode in lista_inodes:
        if inode.nome == nomeLink:
            print(f"Erro: Nome {nomeLink} já está sendo usado.")
            return lista_inodes
        
    # Cria um novo Inode para o diretório
    lista_inodes.append(Inode(nomeLink, "eu", data_criacao_formatada)) # Cria o iNode e adiciona na lista de iNodes
    lista_inodes[len(lista_inodes)-1].ponteiros_iNodes.append(nomeInode)

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual == inode.nome:
            # Adiciona um ponteiro para esse novo iNode, no diretório atual
            lista_inodes[i].ponteiros_iNodes.append(nomeLink)

            print(f"Link {nomeLink} adicionado ao diretório {diretorioAtual}.")
            break
    
    print(f"Link {nomeLink} criado com sucesso.")
    
    return lista_inodes
