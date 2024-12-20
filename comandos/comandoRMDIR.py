from i_node import Inode

def rmdir(nomeDiretorio, lista_inodes, diretorioAtual):
    # Função que remover um diretório

    for i, inode in enumerate(lista_inodes):
        # Verifica se o inode existe
        if nomeDiretorio == inode.nome:
            # Se o iNode existir, exclui ele da lista de iNodes
            if inode.ponteiros_iNodes[0] == 'vazio':
                lista_inodes.pop(i)
                for j, inode_externo in enumerate(lista_inodes):
                    for k, ponteiro in enumerate(inode_externo.ponteiros_iNodes):
                        # Percorre cada iNode, removendo o ponteiro para o 
                        # iNode que foi excluido
                        if nomeDiretorio == ponteiro:
                            lista_inodes[j].ponteiros_iNodes.pop(k)
                            print(f'Ponteiro {ponteiro} removido do iNode {inode_externo.nome}')
                            print(f'Nova lista de ponteiros do Inode {inode_externo.nome}: {lista_inodes[j].ponteiros_iNodes}')
                print(f"Diretório '{nomeDiretorio}' removido com sucesso.")
                break
            else:
                print("Erro: Diretório não está vazio")
                break
        elif i == len(lista_inodes)-1:
            print(f"Erro: O diretório '{nomeDiretorio}' não existe.")

    # print(f"Diretório '{nomeDiretorio}' removido com sucesso.")
        
    return lista_inodes