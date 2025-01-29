from i_node import Inode
from comandos.permissoes import verificaPermissao

# funcao para retornar o id diretorio que deve ser removido caso esteja vazio
def encontra_arquivo(entrada,diretorioAtual, lista_inodes):
    id_inode = None
    idPai = None
    caminho = diretorioAtual.split("/")

    print(entrada,diretorioAtual)
    for posicao in range(len(caminho)):
        for i,inode in enumerate(lista_inodes):
            if inode.nome == caminho[posicao]:
                for filhos in inode.ponteiros_iNodes:
                    for j,inodeP in enumerate(lista_inodes):
                        if posicao == len(caminho) - 1:
                            if inodeP.id == filhos and inodeP.nome == entrada:
                                id_inode = inodeP.id 
                                idPai = inode.id
    print("id:",id_inode)
    print("idPAI:",idPai)
    return id_inode, idPai

def rmdir(nomeDiretorio, lista_inodes, diretorioAtual,usuario_logado):

    id_inode, idPai= encontra_arquivo(nomeDiretorio, diretorioAtual, lista_inodes)
    
    if id_inode != None and idPai != None:
        for i,iNode in enumerate(lista_inodes):
            if iNode.id == id_inode:
                permissoes = verificaPermissao(usuario_logado,lista_inodes,iNode.id)
                
                if "w" in permissoes:
                
                    print("aqui",iNode.ponteiros_iNodes)
                    if iNode.ponteiros_iNodes[0] == "vazio" or iNode.ponteiros_iNodes[0] == []:
                        lista_inodes.remove(id_inode)
                        for j,iNodePai in enumerate(lista_inodes):
                            if iNodePai.id == idPai:
                                iNodePai.ponteiros_iNodes.remove(id_inode)
                    else:
                        print("Diretório não está vazio")
                else: 
                    print("O usuário não possui permissão")
    else:
        print("Diretório não encontrado")
    # Função que remove um diretório
    # diretorioEncontrado = False
    # for iNode in lista_inodes:
    #     if diretorioPai == iNode.nome: #home
    #         for index, idFilho in enumerate(iNode.ponteiros_iNodes):
    #             for idx, i in enumerate(lista_inodes):
    #                 if idFilho == i.id and i.nome == nomeDiretorio:
    #                     diretorioEncontrado = True
    #                     if i.ponteiros_iNodes[0] == 'vazio':
    #                         iNode.ponteiros_iNodes.pop(index)
    #                         print(f"Diretório '{nomeDiretorio}' removido com sucesso.")
    #                     else:
    #                         f"Erro: Diretório {nomeDiretorio} não está vazio."
    
    # if not diretorioEncontrado:
    #     print(f"Erro: O diretório '{nomeDiretorio}' não existe.")

    return lista_inodes