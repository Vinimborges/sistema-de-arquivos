# funcao para retornar o id do arquivo renomeado
def encontra_arquivo(entrada,diretorioAtual, lista_inodes):
    id = None
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
                                id = inodeP.id 
                                idPai = inode.id
    # print("id:",id)
    # print("idPAI:",idPai)
    return id

def mv(diretorioAtual, diretorioPai, lista_inodes, lista_blocos, entrada):
    arquivo = entrada[0]
    diretorio = entrada[1]
    idArquivoDiretorio = None
    idDiretorio = None
    idDiretorioPai = None

    # Encontra o id do arquivo ou diretorio
    for i,iNode in enumerate(lista_inodes):
        if diretorioPai == iNode.nome:
            idDiretorioPai = iNode.id
            for k in iNode.ponteiros_iNodes:
                for m, iNodeFilho in enumerate(lista_inodes):
                    if k == iNodeFilho.id:
                        if arquivo == iNodeFilho.nome:
                            print("id do arquivo ou diretorio",iNodeFilho.id)
                            idArquivoDiretorio = iNodeFilho.id
                        elif diretorio == iNodeFilho.nome:
                            print("id do diretorio que receberá: ",iNodeFilho.id)
                            idDiretorio = iNodeFilho.id
    
    if idArquivoDiretorio == None or idDiretorio == None:
        print("Algum arquivo não exite")
        return lista_inodes

    # Adiciona o arquivo ou diretorio
    for j,iNode in enumerate(lista_inodes):
        if idDiretorio == iNode.id:
            if idArquivoDiretorio not in iNode.ponteiros_iNodes:
                iNode.ponteiros_iNodes.append(idArquivoDiretorio)
                print(f'lista de iNodes: {iNode.ponteiros_iNodes}')
        if iNode.id == idDiretorioPai:
            iNode.ponteiros_iNodes.remove(idArquivoDiretorio)
            print(f'lista de iNodes do dir Pai: {iNode.ponteiros_iNodes}')


    diretorioAtualSeparado = diretorioAtual.split()
        
    return lista_inodes

def mv_Renomear(diretorioAtual,entrada, lista_inodes):

    arquivo = entrada[1]
    novo_nome = entrada[2]

    id = encontra_arquivo(arquivo,diretorioAtual, lista_inodes)

    for i,iNode in enumerate(lista_inodes):
        if iNode.id == id:
            iNode.nome = novo_nome
    return lista_inodes