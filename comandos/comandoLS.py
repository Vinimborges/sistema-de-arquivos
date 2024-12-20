
def ls(entrada,diretorioPai,diretorioAtual, lista_inodes):
    if len(entrada) > 1:
        print('Too much arguments')
        return diretorioAtual
    
    if diretorioAtual == "home":
        for iNode in lista_inodes:  
            if diretorioPai == iNode.nome:
                for filho in iNode.ponteiros_iNodes:
                    print(filho)
    else:
        caminho = diretorioAtual.split("/")
        caminhoCheck = ""
        for trecho in range(len(caminho)-1):
            for iNode in lista_inodes:
                if caminho[trecho] == iNode.nome:
                    caminhoCheck = iNode.nome
                    if caminho[trecho+1] in iNode.ponteiros_iNodes:
                        caminhoCheck = caminhoCheck +"/"+ caminho[trecho+1]
                        if trecho == len(caminho)-2:
                            for newiNode in lista_inodes:
                                if caminho[trecho+1] == newiNode.nome and caminhoCheck == diretorioAtual:
                                    for item in newiNode.ponteiros_iNodes:
                                        print(item) 
                # else:
                #     print('Diretorio não encontrado')
                #     return diretorioAtual
    
    return diretorioAtual
    