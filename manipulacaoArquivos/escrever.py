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
def escrever_controle_de_blocos(nome_disco):
    '''O disco terá 60000 blocos de armazenamento de dados, logo, cada posição do disco.
    partindo da 0 até a 59999 representa um bloco de armazenamento. Se for 0 está livre para uso, se for 1 
    está ocupado'''
    with open(nome_disco, "r+") as disco:
        conteudo_disco = disco.readlines()
        posicao = 0
        aux = 0
        disco.seek(0)
        while(aux<60000):
            temp = list(conteudo_disco[posicao])
            for i in range(len(temp)):
                aux += 1
                if aux >= 60000:
                    break
                if temp[i] == '\x00':
                    temp[i] = '0'
                    print(f'Escreveu o {aux}')
            conteudo_disco[posicao] = ''.join(temp)
            posicao += 1
        for i, text in enumerate(conteudo_disco):
            disco.write(text)
            
# Escrever "Olá Mundo" no bloco 0
# escrever_em_bloco("disco.txt", 0, "SuperBlock|", 4096)
escrever_em_bloco("disco.txt", 100, "Inodes|", 4096)
# escrever_em_bloco("disco.txt", 100, "arquivo1,eu,eu,10,10/10/10,10/10/10,nenhuma,nenhum,nenhum", 4096)
escrever_controle_de_blocos("disco.txt")