def cat(entrada, diretorioAtual, lista_blocos, lista_inodes):
    controle = 0
    checkVazio = -1
    for Inode in lista_inodes:
        if (Inode.nome == diretorioAtual.split("/")[-1]):
            for idPonteiro, ponteiro in enumerate(Inode.ponteiros_iNodes):
                for i, inode_acessado in enumerate(lista_inodes):
                   
                    if ponteiro == inode_acessado.id and entrada == inode_acessado.nome:
                        # print(f'NOME DO QUE INODE {inode_acessado.nome}')

                        if len(inode_acessado.ponteiros_blocos) == 0:
                            print("Arquivo vazio")
                            return lista_blocos

                        for l,pega in enumerate(inode_acessado.ponteiros_blocos):
                            # print("PEGA:")
                            if pega == []:
                                checkVazio = i
                            print("".join(lista_blocos[pega]))
                            controle = 1
                            break
    if (controle == 1):
        if checkVazio == 0:
            print("Arquivo vazio")
        return lista_blocos
    else:
        print("O arquivo não existe ou não está no diretório atual.")
        return lista_blocos

