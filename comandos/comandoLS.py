
def ls(entrada,diretorioPai,diretorioAtual, lista_inodes):
    if len(entrada) > 2:
        print('Too much arguments')
        return diretorioAtual

    mostrar_permissoes = False
    if len(entrada) == 2:
        if entrada[1] == '-l':
            mostrar_permissoes = True

    caminho = diretorioAtual.split("/")
    if len(caminho) >= 2:
        diretorioPai = caminho[-2]
    else:
        diretorioPai = caminho[-1]

    diretorioAtuall = caminho[-1]
    usuario_atual = caminho[-1]
    #print("Dir Pai:", diretorioPai)
    #print("Dir Atual:", diretorioAtual)

    for i,iNodePai in enumerate(lista_inodes):
        if diretorioPai == iNodePai.nome:
            for idFilho in iNodePai.ponteiros_iNodes:
                for j,iNodeFilho in enumerate(lista_inodes):
                    if idFilho == iNodeFilho.id:
                        if diretorioAtual == "home":
                            print(iNodeFilho.nome)
                        if iNodeFilho.nome == diretorioAtuall:
                            for l,iNodeFilhoDir in enumerate(lista_inodes):
                                if iNodeFilhoDir.id == iNodeFilho.id:
                                    for ids in iNodeFilhoDir.ponteiros_iNodes:
                                        for m, iNodeP in enumerate(lista_inodes):
                                            if ids == iNodeP.id:
                                                if iNodeP.dono == usuario_atual:
                                                    data = data_criacao(iNodeP.data_de_modificacao)
                                                    if iNodeP.permissoes_dono.split('+')[0] == 'r':
                                                        if mostrar_permissoes: 
                                                            print(iNodeP.permissoes_dono,iNodeP.permissoes_outros," ",iNodeP.dono," ",data," ",iNodeP.nome)
                                                        else:
                                                            print(iNodeP.nome)
                                                else: # Caso nao seja o dono 
                                                    if iNodeP.permissoes_outros.split('+')[0] == 'r':
                                                        if mostrar_permissoes: 
                                                            print(iNodeP.permissoes_dono,iNodeP.permissoes_outros," ",iNodeP.dono," ",data," ",iNodeP.nome)
                                                        else:
                                                            print(iNodeP.nome)

    return diretorioAtual   
    


def data_criacao(data_de_modificacao):
    data = data_de_modificacao.split('/')
    dia = data[0] + " "

    if data[1] == '01':
        mes = 'Jan'
    elif data[1] == '02':
        mes = 'Fev'
    elif data[1] == '03':
        mes = 'Mar'
    elif data[1] == '04':
        mes = 'Abr'
    elif data[1] == '05':
        mes = 'Mai'
    elif data[1] == '06':
        mes = 'Jun'
    elif data[1] == '07':
        mes = 'Jul'
    elif data[1] == '08':
        mes = 'Ago'
    elif data[1] == '09':
        mes = 'Set'
    elif data[1] == '10':
        mes = 'Out'
    elif data[1] == '11':
        mes = 'Nov'
    elif data[1] == '12':
        mes = 'Dez'
    else:
        mes = " "
    
    return mes + " " + dia
