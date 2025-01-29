from comandos.permissoes import verificaPermissao

def ls(entrada,diretorioPai,diretorioAtual, lista_inodes, usuario_logado):
    if len(entrada) > 2:
        print('Too much arguments')
        return diretorioAtual
        
    mostrar_permissoes = False
    if len(entrada) == 2:
        if entrada[1] == '-l':
            mostrar_permissoes = True

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual.split("/")[-1] in inode.nome:
            permissoes = verificaPermissao(usuario_logado,lista_inodes,inode.id)

            if "r" in permissoes:
                for id in inode.ponteiros_iNodes:
                    for j, iNodeFilho in enumerate(lista_inodes):
                        if id == iNodeFilho.id:
                            data = data_criacao(iNodeFilho.data_de_modificacao)
                            if mostrar_permissoes:
                                print(iNodeFilho.permissoes_dono,iNodeFilho.permissoes_outros," ",iNodeFilho.dono," ",data," ",iNodeFilho.nome)
                            else:
                                print(iNodeFilho.nome)
            else:
                print("Permission denied")
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
