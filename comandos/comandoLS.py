
def ls(entrada,diretorioPai,diretorioAtual, lista_inodes):
    if len(entrada) > 1:
        print('Too much arguments')
        return diretorioAtual

    # print(f'Diretorio Atual: {diretorioAtual}')
    
    
    if diretorioAtual == "home":
        for i,iNode in enumerate(lista_inodes):  
            if diretorioPai == iNode.nome:
                for filho in iNode.ponteiros_iNodes:
                    for j,iNodeFilho in enumerate(lista_inodes):
                        if filho == iNodeFilho.id:
                            print(iNodeFilho.nome)

    else:
        caminho = diretorioAtual.split("/")
        diretorioPai = caminho[-2]
        diretorioAtuall = caminho[-1]

        for i,iNodePai in enumerate(lista_inodes):
            if diretorioPai == iNodePai.nome:
                for idFilho in iNodePai.ponteiros_iNodes:
                    for j,iNodeFilho in enumerate(lista_inodes):
                        if idFilho == iNodeFilho.id:
                            if iNodeFilho.nome == diretorioAtuall:
                                # print("Diretorio ATuak id:", iNodeFilho.id)
                                for l,iNodeFilhoDir in enumerate(lista_inodes):
                                    if iNodeFilhoDir.id == iNodeFilho.id:
                                        for ids in iNodeFilhoDir.ponteiros_iNodes:
                                            for m, iNodeP in enumerate(lista_inodes):
                                                if ids == iNodeP.id:
                                                    print(iNodeP.nome)
    return diretorioAtual
    