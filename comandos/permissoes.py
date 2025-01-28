def verificaPermissao(usuario_logado, lista_inodes, id_inode):
    # Função que retorna a permissao que o usuário logado possui
    for i, inode in enumerate(lista_inodes):
        if inode.id == id_inode:
            if usuario_logado == inode.dono:
                return inode.permissoes_dono
            else:
                return inode.permissoes_outros