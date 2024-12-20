from i_node import Inode
from datetime import date


def mkdir(nomeDiretorio, lista_inodes, diretorioAtual):
    # Função que cria um diretório

    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')

    for inode in lista_inodes:
        # Verifica se o diretorio já existe no diretório
        if inode.nome == nomeDiretorio:
            print(f"Erro: O diretório {nomeDiretorio} já existe no diretório atual.")
            return lista_inodes

    # Cria um novo Inode para o diretório
    lista_inodes.append(Inode(nomeDiretorio, "eu", data_criacao_formatada)) # Cria o iNode e adiciona na lista de iNodes
    print(lista_inodes[len(lista_inodes)-1].data_de_criacao)

    lista_inodes[len(lista_inodes)-1].ponteiros_iNodes.append('vazio')

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual == inode.nome:
            # Adiciona um ponteiro para esse novo iNode, no diretório atual
            lista_inodes[i].ponteiros_iNodes.append(nomeDiretorio)
            print(lista_inodes[i].ponteiros_iNodes)
            print(f"Diretório {nomeDiretorio} adicionado ao diretório {diretorioAtual}.")
            break
    
    print(f"Diretório {nomeDiretorio} criado com sucesso.")
        
    return lista_inodes