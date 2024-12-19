pos = 0
def gravar_no_disco(mem,lista_controle_blocos,lista_inodes,lista_blocos):
    dados = mem
    string = ""
    print(lista_inodes)
    for i in range(15): 
        # Escreve nas prmeiras 15 linhas do disco que é onde 
        # fica os controle de blocos
        for j in range(4094):
            string = string + lista_controle_blocos.pop(0)
            if len(lista_controle_blocos) == 0:
                break
        string = string + "\n"
        dados[i] = string
        print(string)
        string = ""

    for i,dado in enumerate(dados):
        # Encontra a posicao do iNode na lista que tem todo o conteudo do disco
        if "Inodes|" in dado:
            global posicao
            posicao = i
        
    aux = 0
    string = "Inodes|"
    # print(dados[posicao])
    dado_transformado_lista = list(dados[posicao])
    # print(dado_transformado_lista)
    while(len(lista_inodes) != 0):
        # Percorre a lista da Inodes adicionando cada um na lista que tem todo o conteudo do disco
        string = string + lista_inodes[aux].nome
        string = string + "," + lista_inodes[aux].criador
        string = string + "," + lista_inodes[aux].dono
        string = string + "," + lista_inodes[aux].tam
        string = string + "," + lista_inodes[aux].data_de_criacao
        string = string + "," + lista_inodes[aux].data_de_modificacao
        string = string + "," + lista_inodes[aux].permissoes
        string = string + ","
        
        print(lista_inodes[aux].ponteiros_blocos)
        if len(lista_inodes[aux].ponteiros_blocos) == 0:
            string = string + ";"
        else:
            for k, ponteiro in enumerate(lista_inodes[aux].ponteiros_blocos):
                print(ponteiro)
                if k == 0:
                    string = string + str(ponteiro)
                    
                elif k != 0 and k != len(lista_inodes[aux].ponteiros_blocos):
                    print("chegou aqui")
                    string = string +  "!" + str(ponteiro)
                # elif k == len(lista_inodes[aux].ponteiros_blocos):
        string = string + ","

        # string = string + "|"
        print(lista_inodes[aux].ponteiros_iNodes)
        if len(lista_inodes[aux].ponteiros_iNodes) == 0:
            string = string + ';'
        else:
            for j, ponteiro in enumerate(lista_inodes[aux].ponteiros_iNodes):
                print(ponteiro)
                print(f'chegou')
                if j == 0:
                    string = string + str(ponteiro)
                    
                elif j != 0 and j != len(lista_inodes[aux].ponteiros_iNodes):
                    string = string + "!" + str(ponteiro)
                # elif j == len(lista_inodes[aux].ponteiros_iNodes):
        string = string + "|"
        # string = string + ","
            
        print(string)

        string_transformada_lista = list(string)
        print(string_transformada_lista)
        
        for k in range(len(dado_transformado_lista)-1):
            if len(string_transformada_lista) >= 1:
                dado_transformado_lista[k] = string_transformada_lista.pop(0)
            elif len(string_transformada_lista) == 0:
                break
        dados[posicao] = "".join(dado_transformado_lista)
        
        if len(string_transformada_lista) > 0:
            posicao += 1
            for k in range(len(dado_transformado_lista)-1):
                if len(string_transformada_lista) >= 1:
                    dado_transformado_lista[k] = string_transformada_lista.pop(0)
        print(dados[posicao])
        # string = ""
        
        lista_inodes.pop(0)
    
    
    for i in range(5536, 65536):
        dados[i] = str("".join(lista_blocos.pop(0)))
        
    with open("./disco.txt", "w") as disco:
        # Escreve no disco
        for i, linha in enumerate(dados):
            # print(linha)
            # print(linha.nome)
            disco.write(linha)
        print(f'Conteúdo gravado no disco')
    
                