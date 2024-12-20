
def mv(diretorioAtual, diretorioPai, lista_inodes, lista_blocos, entrada):
    arquivo = entrada[0]
    diretorio = entrada[1]

    print(f'Diretorio: {diretorioAtual},{arquivo},{diretorio}')
    diretorioAtualSeparado = diretorioAtual.split()

    if diretorioPai == 'home':
        #ja esta na lista de iNodes
        for i,iNodePai in enumerate(lista_inodes):  
            if diretorioPai == iNodePai.nome:
                print(f'Diretorio pai na lista de inodes')
                if(arquivo in iNodePai.ponteiros_iNodes and diretorio in iNodePai.ponteiros_iNodes):
                    print('os iNodes estao nesse diretorio')

                    #Verificar se o diretorio de destino é um diretorio
                    for destino in lista_inodes:
                        if destino.nome == diretorio:
                            if len(destino.ponteiros_blocos) == 0:
                                print('Diretorio existente')
                                destino.ponteiros_iNodes.append(arquivo) #Adiciona o iNode inteiro na lista de inodes do destino
                                print(f'ponteiros do diretorio: {destino.ponteiros_iNodes}')
                                
                                iNodePai.ponteiros_iNodes.remove(arquivo)#Remove 
                            else:
                                print('Não é um diretorio válido')  
    else:
        #Procura na lista de iNodes se diretorio Atual tem o arquivo e o diretorio
        diretorioAtual = (diretorioAtual.split('/',1)[-1])
        # diretorioAtual = diretorioAtual[1]

        print(f'Diretorio Atual {diretorioAtual}')

        for iNodeAtual in lista_inodes:  
            if diretorioAtual == iNodeAtual.nome: #Encontra inode 
                print(f'esta no diretorio pai {diretorioAtual} e contem: {iNodeAtual.ponteiros_iNodes}')
                if diretorio in iNodeAtual.ponteiros_iNodes:
                    print(f'Diretorio {diretorio} esta dentro de {iNodeAtual.nome}')

                    #Verificar se o diretorio de destino é um diretorio
                    for destino in lista_inodes:
                        if destino.nome == diretorio: #Verifica se é um diretorio
                            print(f' {destino.nome} é um diretorio que consigo adicionar iNode')
                            if 'vazio' in destino.ponteiros_iNodes:
                                destino.ponteiros_iNodes.pop(0)
                            destino.ponteiros_iNodes.append(arquivo)
                            print(f'lista de {destino.nome} :{destino.ponteiros_iNodes}')
                            iNodeAtual.ponteiros_iNodes.remove(arquivo)
        
    return diretorioAtual

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