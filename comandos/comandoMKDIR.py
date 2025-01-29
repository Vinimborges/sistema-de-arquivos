from i_node import Inode
from datetime import date
id_dir = 0
id_diretorioAtual = 0


def mkdir(nomeDiretorio, lista_inodes, diretorioAtual,usuario_logado):
    # Função que cria um diretório
    usuario_existe = False
    usuario = usuario_logado
    if len(diretorioAtual.split('/')) > 1:
        usuario = diretorioAtual.split('/')[1]  #ex: home/ryan

    for i, inode in enumerate(lista_inodes):
        if inode.nome == 'home':
            for iNodeID in inode.ponteiros_iNodes:
                for i, inodeF in enumerate(lista_inodes):
                    if iNodeID == inodeF.id:
                        if usuario == inodeF.nome:
                            usuario_existe = True
    if usuario_existe:
        criador = usuario
    else:
        criador = 'root'


    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')

    for inode in lista_inodes:
        # Verifica se o diretorio já existe no diretório atual
        if diretorioAtual.split("/")[-1] in inode.nome:
            global id_diretorioAtual
            id_diretorioAtual = inode.id
            for i,ponteiro in enumerate(inode.ponteiros_iNodes):
                for ind_inode, inode_acessado in enumerate(lista_inodes):
                    if ponteiro == inode_acessado.id and nomeDiretorio == inode_acessado.nome:
                        print(f"Erro: O diretório {nomeDiretorio} já existe no diretório atual.")
                        return lista_inodes

    # Cria um novo Inode para o diretório
    lista_inodes.append(Inode(lista_inodes[len(lista_inodes)-1].id+1, nomeDiretorio, criador, data_criacao_formatada)) # Cria o iNode e adiciona na lista de iNodes
    global id_dir

    id_dir = lista_inodes[len(lista_inodes)-1].id
    lista_inodes[len(lista_inodes)-1].ponteiros_iNodes.append('vazio')

    for i, inode in enumerate(lista_inodes):
        if diretorioAtual.split("/")[-1] == inode.nome and inode.id == id_diretorioAtual:
            if 'vazio' in inode.ponteiros_iNodes:
                
                inode.ponteiros_iNodes.pop(0)
            # Adiciona um ponteiro para esse novo iNode, no diretório atual
            lista_inodes[i].ponteiros_iNodes.append(id_dir)
            print(lista_inodes[i].ponteiros_iNodes)
            print(f"Diretório {nomeDiretorio} adicionado ao diretório {diretorioAtual}.")
            break
    
    print(f"Diretório {nomeDiretorio} criado com sucesso.")
        
    return lista_inodes