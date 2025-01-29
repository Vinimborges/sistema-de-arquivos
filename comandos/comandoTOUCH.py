from i_node import Inode
from datetime import date
from comandos.permissoes import verificaPermissao

def touch(entrada, lista_inodes, diretorioAtual,usuario_logado):
    # Função que cria um arquivo 
    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')
    
    usuario_existe = False
    usuario = "root"
    
    
    
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
    # print("criador :",criador)

    # print(lista_inodes[len(lista_inodes)-1].data_de_criacao)
    # nome nao tem extensao, vira .txt
    if len(entrada.split(".")) == 1:
        entrada = entrada + '.txt'
        print(entrada)
    for i, inode in enumerate(lista_inodes):
        # print(inode)
        if diretorioAtual.split("/")[-1] in inode.nome:
            permissoes = verificaPermissao(usuario_logado,lista_inodes,inode.id)
            
            if "w" in permissoes:
                print(permissoes)
                # Adiciona um ponteiro para esse novo iNode, no diretório atual
                for pos_inode, ponteiro_Inode in enumerate(inode.ponteiros_iNodes):
                    for ind_inode, inode_acessado in enumerate(lista_inodes):  
                        if ponteiro_Inode == inode_acessado.id and entrada == inode_acessado.nome:
                            print(f"Erro: O nome {entrada} já está sendo usado")
                            return lista_inodes
                
                lista_inodes.append(Inode(lista_inodes[len(lista_inodes)-1].id + 1,entrada, criador, data_criacao_formatada)) # Cria o iNode e adiciona na lista de iNodes
                if len(lista_inodes[i].ponteiros_iNodes) == 1 and lista_inodes[i].ponteiros_iNodes[0] == 'vazio':
                    lista_inodes[i].ponteiros_iNodes.pop(0)
                print(f'Adicionado o iNode {entrada}, no iNode {inode.nome}')
                lista_inodes[i].ponteiros_iNodes.append(lista_inodes[len(lista_inodes)-1].id)
                print(f'Lista de ponteiros Inodes do Inode {inode.nome}: {lista_inodes[i].ponteiros_iNodes}')
                print(f'Nome do arquivo criado: {lista_inodes[len(lista_inodes)-1].nome}')
            else:
                print("O usuário não possui permissão para criar um novo arquivo")
    # for pos in enumerate(lista_inodes):
    #     print(pos[1].nome)
    return lista_inodes