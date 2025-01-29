from comandos.permissoes import verificaPermissao

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

    arquivo_diretorio = entrada[2]
    permissao = entrada[1]
    permissaoDono, permissaoOutros = controlePermissoes(permissao)

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual.split("/")[-1] in inode.nome:
            for id in inode.ponteiros_iNodes:
                for j, iNodeFilhos in enumerate(lista_inodes):
                    if iNodeFilhos.id == id:
                        permissoes = verificaPermissao(usuario_logado,lista_inodes,iNodeFilhos.id)
                        if "w" in permissoes:
                            if iNodeFilhos.nome == arquivo_diretorio:
                                iNodeFilhos.permissoes_dono = permissaoDono
                                iNodeFilhos.permissoes_outros = permissaoOutros
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

    return permissaoDono, permissaoOutros