from datetime import date

def apaga(lista_blocos, lista_inodes, lista_controle_blocos, entrada):
    for inode in lista_inodes:
            # print(f'Entrada: {entrada} inode.nome {inode.nome}')
            if entrada in inode.nome:
                for bloco in inode.ponteiros_blocos:
                    conteudo_bloco = list(lista_blocos[bloco])
                    for k, letra in enumerate(conteudo_bloco):
                        if letra != '\x00':
                            conteudo_bloco[k] = '\x00'
                            
                        
                        
                    lista_blocos[bloco] = conteudo_bloco
                break
    return lista_blocos
                  
                    
                        

def sobrescreve(conteudo, lista_blocos, lista_inodes, lista_controle_blocos, entrada):
    lista_conteudo = list(conteudo)
    #print(lista_conteudo)
    data_modificacao = date.today()
    data_modificacao_formatada = data_modificacao.strftime('%d/%m/%Y')
    apaga(lista_blocos, lista_inodes, lista_controle_blocos, entrada)
    
    
    for i,inode in enumerate(lista_inodes):
        # print(f'Entrada: {entrada} inode.nome {inode.nome}')
        if entrada in inode.nome:
            for j, bloco in enumerate(inode.ponteiros_blocos):
                conteudo_bloco = list(lista_blocos[bloco])
                for k, letra in enumerate(conteudo_bloco):
                    if letra == '\x00' and lista_conteudo:
                        l = k
                        while(len(lista_conteudo) != 0):
                            conteudo_bloco[l] = lista_conteudo.pop(0)
                            l += 1
                            #print("".join(conteudo_bloco))
                            
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
                        if entrada in inode.nome:
                            # print(lista_inodes[z].ponteiros_blocos)
                            lista_inodes[z].ponteiros_blocos.append(j)
                            # print(lista_inodes[z].ponteiros_blocos)
                    if len(lista_conteudo) == 0:
                        lista_inodes[i].tam = str(len(lista_inodes[i].ponteiros_blocos)*4)
                        print(f'Tamanho do arquivo {lista_inodes[i].nome}: {lista_inodes[i].tam}MB')
                        break
            lista_inodes[i].data_de_modificacao = data_modificacao_formatada


    #print("ECHO: ", lista_blocos[0])
    return lista_inodes, lista_controle_blocos, lista_blocos


def cp(entrada1, entrada2, lista_blocos, lista_inodes, lista_controle_blocos):
    
    for Inode1 in lista_inodes:
        if (Inode1.nome == entrada1):
            for Inode2 in lista_inodes:
                if (Inode2.nome == entrada2):
                    for conteudo_arq1 in Inode1.ponteiros_blocos:
                        sobrescreve(lista_blocos[conteudo_arq1], lista_blocos, lista_inodes, lista_controle_blocos, entrada2)
                        #escreve
            break
    return lista_blocos