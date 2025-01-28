def chmod(entrada, diretorioAtual, lista_inodes, usuario_logado):
    if len(entrada) < 3:
        print('Missing arguments')
        return diretorioAtual

    caminho = diretorioAtual.split("/")
    if len(caminho) >= 2:
        diretorioPai = caminho[-2]
    else:
        diretorioPai = caminho[-1]

    diretorioAtuall = caminho[-1]
    usuario_atual = caminho[-1]
    # print("Dir Pai: ", diretorioPai)
    # print("Dir Atual: ", diretorioAtual)
    # print("Usuario Atual: ",usuario_atual)

    # print("entrada",entrada)
    arquivo_diretorio = entrada[2]
    permissao = entrada[1]
    permissaoDono, permissaoOutros = controlePermissoes(permissao)

    #Percorrer
    for i,iNodePai in enumerate(lista_inodes):
        if diretorioPai == iNodePai.nome:
            for idFilho in iNodePai.ponteiros_iNodes:
                for j,iNodeFilho in enumerate(lista_inodes):
                    if idFilho == iNodeFilho.id:
                        # if diretorioAtual == "home":
                        #     print(iNodeFilho.nome)
                        if iNodeFilho.nome == diretorioAtuall:
                            for l,iNodeFilhoDir in enumerate(lista_inodes):
                                if iNodeFilhoDir.id == iNodeFilho.id:
                                    for ids in iNodeFilhoDir.ponteiros_iNodes:
                                        for m, iNodeP in enumerate(lista_inodes):
                                            if ids == iNodeP.id:
                                                if iNodeP.dono == usuario_logado or iNodeP.permissoes_outros[2] == 'w': # Verifica se tem permissao 
                                                    if iNodeP.nome == arquivo_diretorio:
                                                        iNodeP.permissoes_dono = permissaoDono
                                                        iNodeP.permissoes_outros = permissaoOutros
                                                else:
                                                    print("Permission denied")
    return diretorioAtual


def controlePermissoes(permissao):
    permissaoDono = int(permissao[0])
    permissaoOutros = int(permissao[1])
    
    if permissaoDono == 7:
        permissaoDono = 'r+w+x'
    elif permissaoDono == 6:
        permissaoDono = 'r+w+-'
    elif permissaoDono == 5:
        permissaoDono = 'r+-+x'
    elif permissaoDono == 4:
        permissaoDono = 'r+-+x'
    elif permissaoDono == 3:
        permissaoDono = 'r--+x'
    elif permissaoDono == 2:
        permissaoDono = '--+x'
    elif permissaoDono == 1:
        permissaoDono = '---+x'
    elif permissaoDono == 0:
        permissaoDono = '---'

    if permissaoOutros == 7:
        permissaoOutros = 'r+w+x'
    elif permissaoOutros == 6:
        permissaoOutros = 'r+w+-'
    elif permissaoOutros == 5:
        permissaoOutros = 'r+-+x'
    elif permissaoOutros == 4:
        permissaoOutros = 'r+-+x'
    elif permissaoOutros == 3:
        permissaoOutros = 'r--+x'
    elif permissaoOutros == 2:
        permissaoOutros = '--+x'
    elif permissaoOutros == 1:
        permissaoOutros = '---+x'
    elif permissaoOutros == 0:
        permissaoOutros = '---'

    # print("permissao Dono:",permissaoDono)
    # print("permissao Outros:",permissaoOutros)
    return permissaoDono, permissaoOutros