from comandos.comandoTOUCH import touch
from datetime import date

def echo_cria(entrada, lista_inodes, conteudo, lista_controle_blocos, lista_blocos, diretorioAtual):
    lista_conteudo = list(conteudo)
    # print(lista_conteudo)
    # string_conteudo = '"'.join(conteudo).replace('"', "")

    # print(lista_conteudo)
        
    touch(entrada,lista_inodes, diretorioAtual)
    for i,bloco in enumerate(lista_controle_blocos):
        if "0" in bloco:
            conteudo_bloco = list(lista_blocos[i])
            print(f'Bloco {i} está livre, será adicionado conteúdo aqui')
            lista_controle_blocos[i] = "1"
            for j in range(len(lista_conteudo)):
                # print(lista_conteudo.pop(0))
                conteudo_bloco[j] = lista_conteudo.pop(0)
            lista_blocos[i] = conteudo_bloco
            # print(lista_blocos[i])
            for k,inode in enumerate(lista_inodes):
                if entrada == inode.nome:
                    # print(lista_inodes[k].ponteiros_blocos)
                    lista_inodes[k].ponteiros_blocos.append(i)
                    # print(lista_inodes[k].ponteiros_blocos)
                    lista_inodes[k].tam = str(len(lista_inodes[k].ponteiros_blocos) *4) 
            if len(lista_conteudo) == 0:
                break
    return lista_inodes, lista_controle_blocos, lista_blocos

def echo_adiciona(entrada, lista_inodes, conteudo, lista_controle_blocos, lista_blocos, diretorioAtual):
    lista_conteudo = list(conteudo)
    print(lista_conteudo)
    data_modificacao = date.today()
    data_modificacao_formatada = data_modificacao.strftime('%d/%m/%Y')
    
    for i,inode in enumerate(lista_inodes):
        # print(f'Entrada: {entrada} inode.nome {inode.nome}')
        if entrada in inode.nome:
            for j, bloco in enumerate(inode.ponteiros_blocos):
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
        elif i == len(lista_inodes)-1 and entrada != inode.nome:
            echo_cria(entrada, lista_inodes, conteudo, lista_controle_blocos, lista_blocos, diretorioAtual)
            break
    #print("ECHO: ", lista_blocos[0])
    return lista_inodes, lista_controle_blocos, lista_blocos