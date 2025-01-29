from comandos.permissoes import verificaPermissao

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
    return id

def mv(diretorioAtual, diretorioPai, lista_inodes, lista_blocos, entrada, usuario_logado):
    arquivo = entrada[0]
    diretorio = entrada[1]
    idArquivoDiretorio = None
    idDiretorio = None
    idDiretorioPai = None

    if diretorio == "home":
        return lista_inodes

    if diretorio == ".." or diretorio == diretorioAtual.split('/')[-2]:
        diretorio = diretorioAtual.split('/')[-2]
        print("diretorio destino",diretorio)
        for i, inode in enumerate(lista_inodes):
            if diretorio in inode.nome:
                idDiretorio = inode.id
        for i, inode in enumerate(lista_inodes):
            if diretorioAtual.split("/")[-1] in inode.nome:
                idDiretorioPai = inode.id

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual.split("/")[-1] in inode.nome:
            permissao_diretorio = verificaPermissao(usuario_logado,lista_inodes,inode.id)
            
            if "w" in permissao_diretorio: #permissao para mover no diretorio
                print("A")
                for idFilhos in inode.ponteiros_iNodes:
                    for m, iNodeFilho in enumerate(lista_inodes):
                        if idFilhos == iNodeFilho.id:
                            print("teste:",iNodeFilho.nome)
                            if iNodeFilho.nome == arquivo:
                                permissao_diretorio_ar_dir = verificaPermissao(usuario_logado,lista_inodes,iNodeFilho.id)
                                if "w" in permissao_diretorio_ar_dir:
                                    idArquivoDiretorio = iNodeFilho.id

                            if iNodeFilho.nome == diretorio:
                                is_diretorio = tipo_inode(lista_inodes, iNodeFilho.id)
                                if is_diretorio:
                                    permissao_diretorio_destino = verificaPermissao(usuario_logado,lista_inodes,iNodeFilho.id)
                                    if "w" in permissao_diretorio_destino:
                                        idDiretorio = iNodeFilho.id
                                        idDiretorioPai = inode.id
                                    else:
                                        print(permissao_diretorio_destino)
                                        print("Permission denied")
                                        return lista_inodes
                                else: 
                                    print("It is not a folder")
            else:
                print("ARUI,",permissao_diretorio)
                print("Permission denied")
                return lista_inodes

    if not idDiretorio:
        print(f"mv: cannot stat '{arquivo}': No such file or directory")
        return lista_inodes

    if idDiretorio and idArquivoDiretorio and idDiretorioPai:
        # Adiciona o arquivo ou diretorio
        for j,iNode in enumerate(lista_inodes):
            if idDiretorio == iNode.id:
                if idArquivoDiretorio not in iNode.ponteiros_iNodes:
                    iNode.ponteiros_iNodes.append(idArquivoDiretorio)
                    print(f'lista de iNodes: {iNode.ponteiros_iNodes}')
            if iNode.id == idDiretorioPai:
                iNode.ponteiros_iNodes.remove(idArquivoDiretorio)
                print(f'lista de iNodes do dir Pai: {iNode.ponteiros_iNodes}')

    return lista_inodes

def mv_Renomear(diretorioAtual,entrada, lista_inodes, usuario_logado):

    arquivo = entrada[1]
    novo_nome = entrada[2]

    id = encontra_arquivo(arquivo,diretorioAtual, lista_inodes)

    for i,iNode in enumerate(lista_inodes):
        if iNode.id == id:
            iNode.nome = novo_nome
    return lista_inodes


def tipo_inode(lista_inodes, idInode):
    print("ID",idInode)

    for i,inode in enumerate(lista_inodes):
        if inode.id == idInode:
            if len(inode.ponteiros_iNodes) > 0:
                print("diretorio sim")
                return True
            else:
                return False
    return False