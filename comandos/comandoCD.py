# from manipulacaoArquivos import controle_inodes
# from manipulacaoArquivos import ler_memoria

# mem = ler_memoria.Ler_memoria() # Lê toda a memória
# lista_inodes = controle_inodes.Controle_inodes(mem) # Cria uma lista com os Inodes

def cd(entrada,diretorioPai,diretorioAtual, lista_inodes):
    if len(entrada) == 1:
            print(f'Missing a argument') 
            return diretorioAtual
    if len(entrada) > 2:
        print(f'Too much arguments')
        return diretorioAtual
    
    if entrada[1] == ".":
            return diretorioAtual
        
    elif entrada[1] == "..":
        diretorioAnterior = diretorioAtual.rsplit("/",2)
        if (diretorioAnterior[0] + "/") == 'home/':
            return 'home'
        return diretorioAnterior[0] + "/"

    else:
        diretorio = entrada[1]
        print(f'quero ir para {diretorio} ')
        print(f'quero ir para {diretorioAtual} ')

        if diretorioAtual == "home":
            for iNodePai in lista_inodes:  
                if diretorioPai == iNodePai.nome:
                    if(diretorio in iNodePai.ponteiros_iNodes):
                        # print(f'{diretorio} filho de {diretorioPai}')
                        return diretorioAtual + "/" + diretorio
        else:
            caminho = diretorioAtual.split("/")
            caminhoCheck = ""
            print(f'Caminho: {caminho}')
            # for trecho in range(len(caminho)-1):
                 
            for iNodeAtual in lista_inodes:  
                if diretorioAtual == iNodeAtual.nome: #Verifica lista de iNodes do diretorio
                    print(f'lista do diretorio {iNodePai.ponteiros_iNodes}')
                    
                    for filho in lista_inodes: #Verifica se o filho esta na lista de inodes
                        if diretorio in filho.ponteiros_iNodes and len(filho.ponteiros_iNodes) >= 1:
                            print(f'{diretorio} filho de {diretorioPai}')
                            return diretorioAtual + "/" + diretorio
 
        # print(f'{entrada[1]} não encontrado')
        return diretorioAtual