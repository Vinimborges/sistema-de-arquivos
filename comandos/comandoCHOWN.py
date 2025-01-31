from comandos.permissoes import verificaPermissao
# chown username file.txt
id_diretorioAtual = 0
inode_exist = False
user_exist = False

def chown(entrada, diretorioPai, diretorioAtual, lista_inodes, lista_users, usuario_logado):
    # verifica se existem 3 argumentos na entrada
    if len(entrada) < 3:
        print('Erro: Argumentos faltando')
        return diretorioAtual

    arquivo_diretorio = entrada[2]

    # verifica se o nome do novo dono esta na lista de usuários
    usuarios = []
    for i in lista_users:
        usuarios.append(i["user"])


    if entrada[1] not in usuarios:
        print("Erro: usuário inválido")
        return


    # Verifica se nome do iNode existe
    for inode in lista_inodes:
        if diretorioAtual.split("/")[-1] in inode.nome:
            for id in inode.ponteiros_iNodes:
                for j, iNodeFilhos in enumerate(lista_inodes):
                    if iNodeFilhos.id == id:
                        inode_exist = True
                        permissoes = verificaPermissao(usuario_logado,lista_inodes,iNodeFilhos.id)
                        # print(permissoes)
                        # se o iNode tiver permissão de escrita (w)
                        if "w" in permissoes:
                            if iNodeFilhos.nome == arquivo_diretorio:
                                iNodeFilhos.dono = entrada[1]
                                print(f"Dono do {entrada[2]} alterado com sucesso!")
                        else:
                            print("Erro: permissão negada")
                                
    # caso o iNode não exista, exibe uma mensagem de erro
    if not inode_exist:
        print(f"Erro: Este arquivo ou diretório não existe")
        return diretorioAtual





