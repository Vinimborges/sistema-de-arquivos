def escrever_em_bloco(nome_disco, numero_bloco, conteudo, tamanho_bloco):
    with open(nome_disco, "r+") as disco:
        conteudo_disco = disco.readlines()
        posicao = numero_bloco
        aux = 0
        temp = list(conteudo_disco[posicao])
        disco.seek(0)
        while(True):
            if temp[aux] == '\x00':
                for i in conteudo:
                    temp[aux] = i
                    aux += 1
                conteudo_disco[posicao] = ''.join(temp)
                print(conteudo_disco[posicao])
                for i, text in enumerate(conteudo_disco):
                    disco.write(text)
                break
            else:
                aux += 1
            # print(disco.readline())
            # if disco.readline() == None:
            #     conteudo_binario = conteudo[:tamanho_bloco]
            #     conteudo_binario += "\0" * (tamanho_bloco - len(conteudo_binario) - 2)  # Preenche com zeros
            #     conteudo_binario += "\n"
            #     disco.write(conteudo_binario)
            #     break
            # else:
            #     posicao += 1

# Escrever "Olá Mundo" no bloco 0
# escrever_em_bloco("disco.txt", 0, "SuperBlock|", 4096)
# escrever_em_bloco("disco.txt", 100, "Inodes|", 4096)
# escrever_em_bloco("disco.txt", 100, "arquivo1,eu,eu,10,10/10/10,10/10/10,nenhuma,nenhum,nenhum", 4096)