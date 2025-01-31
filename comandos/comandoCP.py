from datetime import date
from comandos.permissoes import verificaPermissao

def apaga(lista_blocos, lista_inodes, lista_controle_blocos, id):
    for i, inode in enumerate(lista_inodes):
        # print(f'Entrada: {entrada} inode.nome {inode.nome}')
        if id == inode.id:
            for bloco in inode.ponteiros_blocos:
                lista_controle_blocos[bloco] = '0'
                lista_inodes[i].ponteiros_blocos.pop(0)
            break
                  

def encontra_arquivo(entrada,diretorioAtual, lista_inodes):
    id = None
    idPai = None
    caminho = diretorioAtual.split("/")

    print(entrada,diretorioAtual)
    for posicao in range(len(caminho)):
        for i,inode in enumerate(lista_inodes):
            if inode.nome == caminho[posicao]:
                for filhos in inode.ponteiros_iNodes:
                    for j,inodeP in enumerate(lista_inodes):
                        if posicao == len(caminho) - 1:
                            if inodeP.id == filhos and inodeP.nome == entrada:
                                id = inodeP.id 
                                idPai = inode.id
    return id

def sobrescreve(entrada, conteudo, lista_blocos, lista_inodes, lista_controle_blocos, diretorioAtual):
 # Função que adiciona o conteúdo se o arquivo já existir
    # ou se não existir, cria um arquivo novo

    lista_conteudo = list(conteudo)
    print(lista_conteudo)
    data_modificacao = date.today()
    data_modificacao_formatada = data_modificacao.strftime('%d/%m/%Y')
    
    for i,inode in enumerate(lista_inodes):
        # Percorre a lista de iNodes para ver se o arquivo já existe
        # print(f'Entrada: {entrada} inode.nome {inode.nome}')
        if diretorioAtual.split("/")[-1] == inode.nome:
            
            for j, inode_filho in enumerate(inode.ponteiros_iNodes):
                for indice, inode_da_lista in enumerate(lista_inodes):
                    
                    if inode_filho == inode_da_lista.id and entrada == inode_da_lista.nome:   
                        global id_inode
                        id_inode = inode_da_lista.id
  
                        
                        for ind_bloco, bloco in enumerate(inode_da_lista.ponteiros_blocos):
                            # Encontra algum bloco que ainda pode ser adicionado texto

                            conteudo_bloco = list(lista_blocos[bloco])
                            for k, letra in enumerate(conteudo_bloco):

                                l = k
                                while(len(lista_conteudo) != 0):
                                    conteudo_bloco[l] = lista_conteudo.pop(0)
                                    l += 1
                                    # print("".join(conteudo_bloco))
                                
                            
                            for letra in conteudo_bloco:
                                if conteudo_bloco[l + 1] != '\x00':
                                    conteudo_bloco[l + 1] = '\x00' 
                                    print(conteudo_bloco)
                            
                            lista_blocos[bloco] = conteudo_bloco

                if len(lista_conteudo) > 0:
                    
                    for k,bloco in enumerate(lista_controle_blocos):
                        # Se todos os blocos estiverem cheio, adiciona em um bloco vazio
                        if "0" in bloco:
                            conteudo_bloco = list(lista_blocos[i])
                            print(f'Bloco {k} está livre, será adicionado conteúdo aqui')
                            lista_controle_blocos[k] = "1"
                            for y in range(len(lista_conteudo)):
                                # print(lista_conteudo.pop(0))
                                conteudo_bloco[y] = lista_conteudo.pop(0)
                                
                            lista_blocos[k] = conteudo_bloco
                            # print(lista_blocos[k])
                            for z,inode1 in enumerate(lista_inodes):
                                print(id_inode)
                                if id_inode == inode1.id:
                                    # print(lista_inodes[z].ponteiros_blocos)
                                    lista_inodes[z].ponteiros_blocos.append(k)
                                    # print(lista_inodes[z].ponteiros_blocos)
                            if len(lista_conteudo) == 0:
                                lista_inodes[i].tam = str(len(lista_inodes[i].ponteiros_blocos)*4) #Adiciona o tamanho do arquivo no iNode
                                print(f'Tamanho do arquivo {lista_inodes[i].nome}: {lista_inodes[i].tam}MB')
                                break
                lista_inodes[i].data_de_modificacao = data_modificacao_formatada # Adiciona a data de modificação no iNode
    #print("ECHO: ", lista_blocos[0])
    return lista_inodes, lista_controle_blocos, lista_blocos


def cp(entrada1, entrada2, lista_blocos, lista_inodes, lista_controle_blocos, diretorioAtual, usuario_logado):
                                    
    entrada1_encontrada = encontra_arquivo(entrada1, diretorioAtual, lista_inodes)
    permissoes_arq1 = verificaPermissao(usuario_logado, lista_inodes, entrada1_encontrada)

    # Permissão de leitura:
    if 'r' in permissoes_arq1:
        entrada2_encontrada = encontra_arquivo(entrada2, diretorioAtual, lista_inodes)
        permissoes_arq2 = verificaPermissao(usuario_logado, lista_inodes, entrada2_encontrada)

        # Permissão de escrita e execução:
        if 'w' in permissoes_arq2:
            if 'x' in permissoes_arq2:

                if entrada1_encontrada != None and entrada2_encontrada != None:
                    apaga(lista_blocos, lista_inodes, lista_controle_blocos, entrada2_encontrada)

                    for ponteiro in lista_inodes[entrada1_encontrada].ponteiros_blocos:
                        for id_bloco, conteudo_copiado in enumerate(lista_blocos):
                            if id_bloco == ponteiro:
                                sobrescreve(entrada2, conteudo_copiado, lista_blocos, lista_inodes, lista_controle_blocos, diretorioAtual)

        

                #else: 
                #print(f'{entrada1} não existe, ou nõa está no diretório atual.')

            else:
                print("Usuário não possui permissão para executar")   

        else:
            print("Usuário não possui permissão para escrever")   

    else: 
        print("Usuário não possui permissão para ler")                



    


#     #entrada2 recebe o conteudo de entrada1
#     for (Inode1 in lista_inodes):
#         if (Inode1.nome == diretorioAtual):
#             for (ponteiros1 in Inode1.ponteiros_iNodes):
#                 for (id_iNodes1 in lista_inodes):
#                     if (ponteiros1 == id_iNodes1.id and entrada1 == id_iNodes1.nome): #id_iNodes == entrada1
#                         for (ponteiros2 in Inode2.ponteiros_iNodes):
#                             for (id_iNodes2 in lista_inodes):
#                                 if (ponteiros2 == id_iNodes2.id and entrada2 == id_iNodes2.nome): #id_iNodes == entrada1
#                                     for (conteudo_copiado in id_iNodes1.ponteiros_blocos):
#                                         sobrescreve(lista_blocos[conteudo_copiado], lista_blocos, lista_inodes, lista_controle_blocos, id_iNodes2.id, diretorioAtual)
                   
                        
    return lista_blocos