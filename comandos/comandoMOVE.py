
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
        diretorioPai = diretorioPai.split('/')
        diretorioPai = diretorioPai[1]
        print(f'Diretorio pai {diretorioPai}')

        for iNodePai in lista_inodes:  
            if diretorioPai == iNodePai.nome: #Encontra inode 
                print(f'esta no diretorio pai {diretorioPai} e lista: {iNodePai.ponteiros_iNodes}')

                if(arquivo in iNodePai.ponteiros_iNodes and diretorio in iNodePai.ponteiros_iNodes):
                    print('os iNodes estao nesse diretorio')

                    #Verificar se o diretorio de destino é um diretorio
                    for destino in lista_inodes:
                        if destino.nome == diretorio and (destino.ponteiros_iNodes) >= 1: #Verifica se é um diretorio
                            if len(destino.ponteiros_blocos) == 0:
                                print('Diretorio existente')
                                destino.ponteiros_iNodes.append(arquivo) #Adiciona o iNode inteiro na lista de inodes do destino
                                print(f'ponteiros do diretorio: {destino.ponteiros_iNodes}')
                                
                                iNodePai.ponteiros_iNodes.remove(arquivo)#Remove 
                            else:
                                print('Não é um diretorio válido')
                else: 
                    print('Um dos dois nao esta no diretorio atual')
        
    

    return diretorioAtual

def mv_Renomear(diretorioAtual):
    return diretorioAtual