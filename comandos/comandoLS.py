
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
        # caminhoCheck = ""
        print(f'caminho: {caminho}')
        print(f'Diretorio Pai: {caminho[-2]}')
        print(f'Diretorio Atual: {caminho[-1]}')
        diretorioPai = caminho[-2]
        diretorio = caminho[-1]

        for iNode in lista_inodes:
            if diretorioPai == iNode.nome:
                if diretorio in iNode.ponteiros_iNodes:
                    for newiNode in lista_inodes:
                        if diretorio == newiNode.nome:
                            for item in newiNode.ponteiros_iNodes:
                                if item != 'vazio':
                                    print(item) 
    
    return diretorioAtual
    