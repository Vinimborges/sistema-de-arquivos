
def ls(entrada,diretorioPai,diretorioAtual, lista_inodes):
    if len(entrada) > 1:
        print(f'Too much arguments')
        return diretorioAtual
    for iNode in lista_inodes:  
        if diretorioPai == iNode.nome:
            for filho in iNode.ponteiros_iNodes:
                print(filho)
    return diretorioAtual
    