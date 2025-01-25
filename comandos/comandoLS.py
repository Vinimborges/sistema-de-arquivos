
def ls(entrada,diretorioPai,diretorioAtual, lista_inodes):
    if len(entrada) > 1:
        print('Too much arguments')
        return diretorioAtual

    caminho = diretorioAtual.split("/")
    if len(caminho) >= 2:
        diretorioPai = caminho[-2]
    else:
        diretorioPai = caminho[-1]

    diretorioAtuall = caminho[-1]
    usuario_atual = caminho[-1]
    #print("Dir Pai:", diretorioPai)
    #print("Dir Atual:", diretorioAtual)

    for i,iNodePai in enumerate(lista_inodes):
        if diretorioPai == iNodePai.nome:
            for idFilho in iNodePai.ponteiros_iNodes:
                for j,iNodeFilho in enumerate(lista_inodes):
                    if idFilho == iNodeFilho.id:
                        if diretorioAtual == "home":
                            print(iNodeFilho.nome)
                        if iNodeFilho.nome == diretorioAtuall:
                            for l,iNodeFilhoDir in enumerate(lista_inodes):
                                if iNodeFilhoDir.id == iNodeFilho.id:
                                    for ids in iNodeFilhoDir.ponteiros_iNodes:
                                        for m, iNodeP in enumerate(lista_inodes):
                                            if ids == iNodeP.id:
                                                if iNodeP.dono == usuario_atual:
                                                    if iNodeP.permissoes_dono.split('+')[0] == 'r':
                                                        print("dono",iNodeP.nome)
                                                else: # Caso nao sej    a o dono 
                                                    if iNodeP.permissoes_outros.split('+')[0] == 'r':
                                                        print("outro",iNodeP.nome)

    return diretorioAtual   
    