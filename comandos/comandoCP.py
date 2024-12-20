from datetime import date

def apaga(lista_blocos, lista_inodes, lista_controle_blocos, id):
    for i, inode in enumerate(lista_inodes):
        # print(f'Entrada: {entrada} inode.nome {inode.nome}')
        if id == inode.id:
            for bloco in inode.ponteiros_blocos:
                lista_controle_blocos[bloco] = '0'
                lista_inodes[i].ponteiros_blocos.pop(0)
            break
                  

def sobrescreve(conteudo, lista_blocos, lista_inodes, lista_controle_blocos, id, diretorioAtual):
    lista_conteudo = list(conteudo)
    print(lista_conteudo)
    data_modificacao = date.today()
    data_modificacao_formatada = data_modificacao.strftime('%d/%m/%Y')
    apaga(lista_blocos, lista_inodes, lista_controle_blocos, id)
    
    for i,inode in enumerate(lista_inodes):
        # Percorre a lista de iNodes para ver se o arquivo já existe
        # print(f'Entrada: {entrada} inode.nome {inode.nome}')
        if diretorioAtual.split("/")[-1] == inode.nome:
            # if entrada in inode.ponteiros_iNodes:
            for j, inode_filho in enumerate(inode.ponteiros_iNodes):
                for indice, inode_da_lista in enumerate(lista_inodes):
                    if inode_filho == inode_da_lista.id:
                        id_inode = inode_da_lista.id
                        for ind_bloco, bloco in enumerate(inode_da_lista.ponteiros_blocos):
                            # Encontra algum bloco que ainda pode ser adicionado texto
                            conteudo_bloco = list(lista_blocos[bloco])
                            for k, letra in enumerate(conteudo_bloco):
                                if letra == '\x00':
                                    l = k
                                    while(len(lista_conteudo) != 0):
                                        conteudo_bloco[l] = lista_conteudo.pop(0)
                                        l += 1
                                        print("".join(conteudo_bloco))
                                        
                                    # print(conteudo_bloco)
                                if len(lista_conteudo) == 0:
                                    lista_blocos[bloco] = conteudo_bloco
                                    break  
                            if len(lista_conteudo) == 0:
                                lista_blocos[bloco] = conteudo_bloco
                                break  
                        if len(lista_conteudo) == 0:
                            lista_blocos[bloco] = conteudo_bloco
                            break  
            
            for j,bloco in enumerate(lista_controle_blocos):
                # Se todos os blocos estiverem cheio, adiciona em um bloco vazio
                if "0" in bloco:
                    conteudo_bloco = list(lista_blocos[i])
                    print(f'Bloco {j} está livre, será adicionado conteúdo aqui')
                    lista_controle_blocos[j] = "1"
                    for k in range(len(lista_conteudo)):
                        # print(lista_conteudo.pop(0))
                        conteudo_bloco[k] = lista_conteudo.pop(0)
                        
                    lista_blocos[j] = conteudo_bloco
                    # print(lista_blocos[j])
                    for z,inode in enumerate(lista_inodes):
                        if id_inode == inode.id:
                            # print(lista_inodes[z].ponteiros_blocos)
                            lista_inodes[z].ponteiros_blocos.append(j)
                            # print(lista_inodes[z].ponteiros_blocos)
                    if len(lista_conteudo) == 0:
                        lista_inodes[i].tam = str(len(lista_inodes[i].ponteiros_blocos)*4) #Adiciona o tamanho do arquivo no iNode
                        print(f'Tamanho do arquivo {lista_inodes[i].nome}: {lista_inodes[i].tam}MB')
                        break
            lista_inodes[i].data_de_modificacao = data_modificacao_formatada # Adiciona a data de modificação no iNode
    
    #print("ECHO: ", lista_blocos[0])
    return lista_inodes, lista_controle_blocos, lista_blocos


def cp(entrada1, entrada2, lista_blocos, lista_inodes, lista_controle_blocos, diretorioAtual):
    #entrada2 recebe o conteudo de entrada1
    for Inode1 in lista_inodes:
        if (Inode1.nome == diretorioAtual):
            for ids in Inode1.ponteiros_iNodes:
                for id_iNodes in lista_inodes:
                    if (ids == id_iNodes.id and entrada1 == id_iNodes.nome): #id_iNodes == entrada1
                        conteudo1 = lista_blocos[id_iNodes.ponteiros_blocos]

            for ids in Inode1.ponteiros_iNodes:
                for id_iNodes in lista_inodes:
                    if (ids == id_iNodes.id and entrada2 == id_iNodes.nome): #id_iNodes == entrada1
                        sobrescreve(conteudo1, lista_blocos, lista_inodes, lista_controle_blocos, id_iNodes.id, diretorioAtual)
                        #escreve
            break
    return lista_blocos