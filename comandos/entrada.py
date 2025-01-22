


from manipulacaoArquivos.gravarNoDisco import gravar_no_disco

# Import dos comandos
from comandos.comandoLS import ls
from comandos.comandoCD import cd
from comandos.comandoCLEAR import clear
from comandos.comandoTOUCH import touch
from comandos.comandoRM import rm
from comandos.comandoECHO import echo_cria, echo_adiciona
from comandos.comandoCAT import cat
from comandos.comandoCP import cp
from comandos.comandoMKDIR import mkdir
from comandos.comandoLN import ln
from comandos.comandoRMDIR import rmdir
from comandos.comandoMOVE import mv, mv_Renomear




# print(lista_blocos[len(lista_blocos)-1])
# print(len(lista_blocos))


        


def tratar_entrada(diretorioAtual,read,mem,lista_inodes,lista_controle_blocos,lista_blocos,lista_users): 
    if diretorioAtual.count("/") == 1: #home
            diretorioPai = '/home'
    else:
        diretorioAtualPartes = diretorioAtual.rsplit("/",2)
        diretorioPai = diretorioAtualPartes[len(diretorioAtualPartes) - 2]
    
    # print(f'Diretorio pai: {diretorioPai}')
    entrada = read.split()

    # VINI (OK) (ok)
    if "touch" in read: # Cria arquivo
        # print(lista_inodes[len(lista_inodes)-1].criador)
        touch(entrada[1], lista_inodes, diretorioAtual)
        # print(lista_inodes[len(lista_inodes)-1].criador)
        return diretorioAtual
    
    # Bia (OK) (OK)
    elif "rmdir" in read: # verificar se ponteiros iNode esta vazia e olhar o pai
        rmdir(entrada[1], lista_inodes, diretorioAtual)
        return diretorioAtual
    
    # VINI (ok) (ok)
    elif "rm" in read: # Remove arquivo
        # procura pelo nome remove da lista temporaria
        print(f'Nome do arquivo excluído: {entrada[1]}')
        rm(entrada[1], diretorioAtual, lista_inodes, lista_controle_blocos)
        return diretorioAtual

    # VINI (OK) (ok)
    elif "echo" in read:
        entrada_echo = read.split(">")
        print(entrada_echo)
        print(type(entrada_echo))
        conteudo = entrada_echo[0].split('"')
        if len(entrada_echo) == 2: #Cria um arquivo já adicionando conteúdo
            echo_cria(entrada_echo[2].replace(" ", ""), lista_inodes, conteudo[1], lista_controle_blocos, lista_blocos, diretorioAtual)
            # print("um")
        elif len(entrada_echo) == 3: #Adiciona conteúdo a um arquivo existente ou cria caso não exista
            echo_adiciona(entrada_echo[2].replace(" ", ""), lista_inodes, conteudo[1], lista_controle_blocos, lista_blocos, diretorioAtual)
            # print("dois")
        return diretorioAtual

    # Ksnoh (OK) (OK)
    elif "cat" in read: # Lê o arquivo
        # olhar pro iNode e ir na posicao da lista do block
        cat(entrada[1], diretorioAtual, lista_blocos, lista_inodes)
        return diretorioAtual

    # Ksnoh (nao testei)
    elif "cp" in read: #Copia arquivo
        # ao criar o iNode copia o bloco do outro iNode
        print(f'Copiando o arquivo {entrada[1]} para o arquivo {entrada[2]}')
        cp(entrada[1], entrada[2], lista_blocos, lista_inodes, lista_controle_blocos, diretorioAtual)
        return diretorioAtual
        
    # Ryan (OK) (OK)
    elif "mv" in read: #Move/Renomeia arquivos
        if "/" in entrada[1]:
            sep = entrada[1].split("/")
            # print(f'Movendo o arquivo:{sep[0]} para o diretório: {sep[1]}')
            mv(diretorioAtual, diretorioPai, lista_inodes, lista_blocos, sep)
        else:
            # print(f'Renomeando o arquivo {entrada[1]} para {entrada[2]}')
            mv_Renomear(diretorioAtual, entrada, lista_inodes)
        return diretorioAtual

    # Bia (nao testei)
    elif "ln" in read: #cria um Inode com os mesmos ponteiros (link)
        ln(entrada[3], entrada[2], lista_inodes, diretorioAtual)
        return diretorioAtual
        
    # Bia (OK)  (ok)
    elif "mkdir" in read: # Cria um diretório e nao tem extesao(criar um inode)
        mkdir(entrada[1], lista_inodes, diretorioAtual)
        return diretorioAtual
            
    # Ryan (OK) (ok)
    elif "ls" in read:  # listar os nome dos ponteiros iNodes
        return ls(entrada, diretorioPai, diretorioAtual, lista_inodes)
            
    # Ryan (OK) (ok)
    elif "cd" in read:  # mover para o bloco do iNode selecionado da lista de iNodes (. permanece no mesmo diretorio, .. move um diretorio para tras)
        return cd(entrada, diretorioPai, diretorioAtual, lista_inodes)

    # Ryan (OK) (ok)
    elif "clear" in read: # encerra o programa
        return clear(diretorioAtual)
        
    #      (OK) (ok)
    elif ("kill" in read) or ("exit" in read): # encerra o programa           
        # print("Programa encerrado")
        gravar_no_disco(mem,lista_controle_blocos,lista_inodes,lista_blocos,lista_users) # Função que grava o conteúdo no disco após o programa ser encerrado
        return "kill"
    
    else:
        print("Comando não reconhecido")
        return diretorioAtual
    