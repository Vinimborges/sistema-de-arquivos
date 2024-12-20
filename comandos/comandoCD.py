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
        print(f'quero ir para {entrada[1]} ')
        print(lista_inodes)
        if entrada[1] in lista_inodes:
            print(f'{entrada[1]} é um diretório')
            return diretorioAtual + "/" + entrada[1]
        
        # for iNode in lista_inodes:
        #     if entrada[1] == iNode.nome:
        #         #checar se é um diretorio
        #         if len(iNode.ponteiros_blocos) >= 0 and len(iNode.ponteiros_iNodes) == 0:
        #             print(f'{entrada[1]} é um diretorio')
        #             # Se é possivel entrar no diretorio
        #             return diretorioAtual + entrada[1] + "/"
        #         print(f'{entrada[1]} não é um diretório')
        #         return diretorioAtual
            
        # print(f'{entrada[1]} não encontrado')
        return diretorioAtual