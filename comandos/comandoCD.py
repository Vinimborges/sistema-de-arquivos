def cd(entrada,diretorioPai,diretorioAtual, lista_inodes, usuario_logado):
    if len(entrada) == 1:
            print(f'Missing a argument') 
            return diretorioAtual
    if len(entrada) > 2:
        print(f'Too much arguments')
        return diretorioAtual
    
    if entrada[1] == ".":
            return diretorioAtual
        
    elif entrada[1] == "..":
        diretorioAnterior = diretorioAtual.rsplit("/",1)
        # print(diretorioAtual)
        # print(diretorioAnterior)
        if (diretorioAnterior[0] + "/") == 'home/':
            return 'home'

        return diretorioAnterior[0]

    else:
        diretorio = entrada[1]
        diretorioAtualFinal = (diretorioAtual.split('/')[-1])
        
        caminho = diretorio.split('.')
        # print(teste)
        if len(caminho) > 1:
            print('Não é possivel entrar em um arquivo')
            return diretorioAtual

        # print(f'quero ir para: {diretorio} ')
        # print(f'dir atual: {diretorioAtualFinal} ')

        for i,iNodePai in enumerate(lista_inodes):
            if iNodePai.nome == diretorioAtualFinal:
                for k, filho in enumerate(iNodePai.ponteiros_iNodes):
                    for i,iNode in enumerate(lista_inodes):
                        if (iNode.dono == usuario_logado or iNode.permissoes_outros[0] == 'r'):
                            if iNode.id == filho and iNode.nome == diretorio:
                                return diretorioAtual + "/" + iNode.nome
                        else:
                            print("Permission denied")
                            return diretorioAtual
        return diretorioAtual