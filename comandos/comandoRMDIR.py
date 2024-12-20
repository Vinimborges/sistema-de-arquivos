from i_node import Inode

def rmdir(nomeDiretorio, lista_inodes, diretorioPai, diretorioAtual):
    # Função que remove um diretório
    diretorioEncontrado = False
    for iNode in lista_inodes:
        if diretorioPai == iNode.nome: #home
            for index, idFilho in enumerate(iNode.ponteiros_iNodes):
                for idx, i in enumerate(lista_inodes):
                    if idFilho == i.id and i.nome == nomeDiretorio:
                        diretorioEncontrado = True
                        if i.ponteiros_iNodes[0] == 'vazio':
                            iNode.ponteiros_iNodes.pop(index)
                            print(f"Diretório '{nomeDiretorio}' removido com sucesso.")
                        else:
                            f"Erro: Diretório {nomeDiretorio} não está vazio."
    
    if not diretorioEncontrado:
        print(f"Erro: O diretório '{nomeDiretorio}' não existe.")

    return lista_inodes