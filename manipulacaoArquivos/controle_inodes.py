from i_node import Inode

def Controle_inodes(lista_conteudo_disco):
    lista_inodes = []
    for i, mem in enumerate(lista_conteudo_disco):
        if "Inodes" in mem or (mem[0] != '\x00' and i > 0): # Função que busca os Inodes que estão salvos na memória
            temp = mem.split("|") # iNode | Dados Inode
            # print(temp)
            temp.pop(0)
            for i, temp in enumerate(temp):
                temp1 = temp.split(",")
                if(temp1[0] != '\x00' and len(temp1) > 1):
                    nome = temp1.pop(0)
                    criador = temp1.pop(0)
                    inode = Inode(nome, criador)
                    inode.dono = temp1.pop(0)
                    inode.tam = temp1.pop(0)
                    inode.data_de_criacao = temp1.pop(0)
                    inode.data_de_modificacao = temp1.pop(0)
                    inode.permissoes = temp1.pop(0)
                    if temp1[0] == ';':
                        # print(f'Lista de ponteiros blocos vazia')
                        temp1.pop(0)
                    else:
                        separar_ponteiros = temp1.pop(0).split("!")
                        # print(separar_pontiros)
                        for j, pointer in enumerate(separar_ponteiros):
                            separar_ponteiros[j] = int(pointer)
                        inode.ponteiros_blocos = separar_ponteiros
                        # print(inode.ponteiros_blocos)
                    # print(temp1[0])
                    # if "\x00" in temp1[0]:
                    #     print('Chegou')
                    #     tirar_zeros = temp1[0].split("\x00")
                        # print(tirar_zeros[0])
                    if temp1[0] == ';':
                        # print(f'Lista de ponteiros iNodes vazia')
                        temp1.pop(0)
                    else:
                        separar_ponteiros = temp1.pop(0).split("!")
                        # print(separar_ponteiros)
                        for j, pointer in enumerate(separar_ponteiros):
                            separar_ponteiros[j] = int(pointer)
                        inode.ponteiros_iNodes = separar_ponteiros
                        # print(inode.ponteiros_iNodes)
                        # inode.ponteiros_iNodes = temp1.pop(0)
                        # print(tirar_zeros)
                    lista_inodes.append(inode)
                    
                    # print(lista_inodes[len(lista_inodes)-1].criador)
                    # print(lista_inodes[0].dono)
                    # print(lista_inodes[0].ponteiros_iNodes)
    return lista_inodes