
from manipulacaoArquivos.ler_memoria import Ler_memoria
from manipulacaoArquivos.controle_blocos import Controle_blocos
from manipulacaoArquivos.controle_inodes import Controle_inodes
from manipulacaoArquivos.blocos import Blocos
from manipulacaoArquivos.gravarNoDisco import gravar_no_disco

# Import dos comandos
from comandos.comandoLS import ls
from comandos.comandoCD import cd
from comandos.comandoCLEAR import clear
from comandos.comandoTOUCH import touch
from comandos.comandoRM import rm
from comandos.comandoECHO import echo_cria, echo_adiciona
from comandos.comandoCAT import cat

mem = Ler_memoria() # Lê toda a memória


lista_inodes = Controle_inodes(mem) # Cria uma lista com os Inodes
lista_controle_blocos = Controle_blocos(mem) # Cria uma lista de blocos livres e ocupados
lista_blocos = Blocos(mem) # Cria uma lista com o conteúdo armazenado nos blocos
# print(lista_blocos[len(lista_blocos)-1])
# print(len(lista_blocos))

espaco_livre = 0

for i in range(len(lista_controle_blocos)-1): # Verifica quanto espaço livre tem
    if lista_controle_blocos[i] == "0":
        espaco_livre += 4


print(f'Espaço livre para armazenamento: {espaco_livre//1028} MB')
        


def tratar_entrada(diretorioAtual,read): 
    if diretorioAtual.count("/") == 1: #home
            diretorioPai = '/home'
    else:
        diretorioAtualPartes = diretorioAtual.rsplit("/",2)
        diretorioPai = diretorioAtualPartes[len(diretorioAtualPartes) - 2]
    
    print(f'Diretorio pai: {diretorioPai}')
    entrada = read.split()

    # VINI
    if "touch" in read: # Cria arquivo
        # print(lista_inodes[len(lista_inodes)-1].criador)
        touch(entrada[1], lista_inodes, diretorioAtual)
        # print(lista_inodes[len(lista_inodes)-1].criador)
        return diretorioAtual
    
    # VINI
    elif "rm" in read: # Remove arquivo
        # procura pelo nome remove da lista temporaria
        print(f'Nome do arquivo excluído: {entrada[1]}')
        rm(entrada[1], lista_inodes, lista_controle_blocos)
        return diretorioAtual

    # VINI
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

    # Ksnoh
    elif "cat" in read: # Lê o arquivo
        # olhar pro iNode e ir na posicao da lista do block
        print(f'Lendo o arquivo: {entrada[1]}')
        cat(entrada[1], diretorioAtual, lista_blocos, lista_inodes)
        # criar_arquivo(entrada[1])
        return diretorioAtual

    # Ksnoh
    elif "cp" in read: #Copia arquivo
        # ao criar o iNode copia o bloco do outro iNode
        print(f'Copiando o arquivo {entrada[1]} para o arquivo {entrada[2]}')
        
    # Ryan
    elif "mv" in read: #Move/Renomeia arquivo
        if "/" in entrada[2]:
            sep = entrada[2].split("/")
            print(f'Movendo o arquivo {entrada[1]} para o diretório {sep[0]} com o nome {sep[1]}')
        else:
            print(f'Renomeando o arquivo {entrada[1]} para {entrada[2]}')

    # Bia
    elif "ln" in read:# cria um Inode com os mesmos ponteiros (link)
        print(f'Criado o link {entrada[3]} para o arquivo {entrada[2]}')
        
    # Bia
    elif "mkdir" in read: # Cria um diretório e nao tem extesao(criar um inode)
        print(f'Nome do diretório criado: {entrada[1]}')
        
    # Bia
    elif "rmdir" in read: # verificar se ponteiros iNode esta vazia e olhar o pai
        print(f'Diretório {entrada[1]} removido')
    
    # Ryan
    elif "ls" in read:  # listar os nome dos ponteiros iNodes
        return ls(entrada,diretorioPai,diretorioAtual)
            
    # Ryan
    elif "cd" in read:  # mover para o bloco do iNode selecionado da lista de iNodes (. permanece no mesmo diretorio, .. move um diretorio para tras)
        return cd(entrada,diretorioPai,diretorioAtual)

    # Ryan
    elif "clear" in read: # encerra o programa
        return clear(diretorioAtual)
        
    elif "kill" in read: # encerra o programa           
        print("Programa encerrado")
        gravar_no_disco(mem,lista_controle_blocos,lista_inodes,lista_blocos) # Função que grava o conteúdo no disco após o programa ser encerrado
        return "kill"
    
    else:
        print("Comando não reconhecido")
        return diretorioAtual
    