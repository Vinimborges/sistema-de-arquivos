
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

    # if diretorioPai == 'home':
    #     #ja esta na lista de iNodes
    #     for i,iNodePai in enumerate(lista_inodes):  
    #         if diretorioPai == iNodePai.nome:
    #             # print(f'Diretorio pai na lista de inodes')
    #             for k, filho in enumerate(iNodePai.ponteiros_iNodes):
    #                 for j, inode in enumerate(lista_inodes):
    #                     if inode.id == filho and inode.nome == diretorio:
    #                         for m, diretorioTeste in enumerate(lista_inodes):
    #                             if diretorioTeste.id == inode.id and len(diretorioTeste.ponteiros_iNodes) >= 1:

    #                                 for i,iNodePais in enumerate(lista_inodes):  
    #                                     if diretorioPai == iNodePais.nome:
    #                                         for k, filhos in enumerate(iNodePais.ponteiros_iNodes):
    #                                             for j, inodes in enumerate(lista_inodes):
    #                                                 if inodes.id == filhos and inodes.nome == arquivo:
    #                                                     diretorioTeste.ponteiros_iNodes.append(inodes.id)
    #                                                     if 'vazio' in diretorioTeste.ponteiros_iNodes:
    #                                                         diretorioTeste.ponteiros_iNodes.pop(0)
    #                                                     print(f"diretorio {diretorioTeste.nome} atualizado {diretorioTeste.ponteiros_iNodes}")

        
    return lista_inodes

def mv_Renomear(diretorioAtual,entrada, lista_inodes):
    diretorioAtual = diretorioAtual.split("/")[-1]
    nomeAtual = entrada[1]
    novoNome = entrada[2]
    # print(f'nA: {nomeAtual}, nN:{novoNome}, diretorio Atual: {diretorioAtual}')

    for i,iNodePai in enumerate(lista_inodes):
        if iNodePai.nome == diretorioAtual:
            # print(f'Cheguei no diretorio {diretorioAtual},{iNodePai.ponteiros_iNodes}')
            for k, filho in enumerate(iNodePai.ponteiros_iNodes):
                for i,iNode in enumerate(lista_inodes):
                    print(iNode.id,':',iNode.nome)
                    if iNode.id == filho and iNode.nome == nomeAtual:
                        iNode.nome = novoNome

    return lista_inodes