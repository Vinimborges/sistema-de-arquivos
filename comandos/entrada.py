from i_node import Inode
from manipulacaoArquivos import ler_memoria
from manipulacaoArquivos import controle_blocos
from manipulacaoArquivos import controle_inodes
from manipulacaoArquivos import blocos

mem = ler_memoria.Ler_memoria() # Lê toda a memória


lista_inodes = controle_inodes.Controle_inodes(mem) # Cria uma lista com os Inodes
lista_controle_blocos = controle_blocos.Controle_blocos(mem) # Cria uma lista de blocos livres e ocupados
lista_blocos = blocos.Blocos(mem) # Cria uma lista com o conteúdo armazenado nos blocos
# print(lista_blocos[len(lista_blocos)-1])
# print(len(lista_blocos))

espaco_livre = 0

for i in range(len(lista_controle_blocos)-1): # Verifica quanto espaço livre tem
    if lista_controle_blocos[i] == "0":
        espaco_livre += 4




print(f'Espaço livre para armazenamento: {espaco_livre//1028} MB')
        
def criar_arquivo(nome):
    # nome nao tem extensao, vira .txt
    lista_inodes.append(Inode(nome, "eu"))
    print(f'Nome do arquivo criado: {lista_inodes[len(lista_inodes)-1].nome}')
    for pos in enumerate(lista_inodes):
        print(pos[1].nome)

def tratar_entrada(read): 
    nome = read.split()

    # VINI
    if "touch" in read: # Cria arquivo
        criar_arquivo(nome[1])
    
    # VINI
    elif "rm" in read: # Remove arquivo
        # procura pelo nome remove da lista temporaria
        print(f'Nome do arquivo excluído: {nome[1]}')
        # remove_arquivo(nome[1])

    # VINI
    elif "echo" in read: 
        # primeiro cria o inode e depois ja escreve no bloco dele
        nome_echo = read.split(">")
        print(nome_echo)
        print(type(nome_echo))
        if len(nome_echo) == 2: #Cria um arquivo já adicionando conteúdo 
            print("um")
        elif len(nome_echo) == 3: #Adiciona conteúdo a um arquivo existente ou cria caso não exista
            print("dois")

    # Ksnoh
    elif "cat" in read: # Lê o arquivo
        # olhar pro iNode e ir na posicao da lista do block  
        print(f'Lendo o arquivo: {nome[1]}')
        # criar_arquivo(nome[1])

    # Ksnoh
    elif "cp" in read: #Copia arquivo
        # ao criar o iNode copia o bloco do outro iNode
        print(f'Copiando o arquivo {nome[1]} para o arquivo {nome[2]}')
        
    # Ryan
    elif "mv" in read: #Move/Renomeia arquivo
        if "/" in nome[2]:
            sep = nome[2].split("/")
            print(f'Movendo o arquivo {nome[1]} para o diretório {sep[0]} com o nome {sep[1]}')
        else:
            print(f'Renomeando o arquivo {nome[1]} para {nome[2]}')

    # Bia
    elif "ln" in read:# cria um Inode com os mesmos ponteiros (link)
        print(f'Criado o link {nome[3]} para o arquivo {nome[2]}')
        
    # Bia
    elif "mkdir" in read: #Cria um diretório e nao tem extesao(criar um inode)
        print(f'Nome do diretório criado: {nome[1]}')
        
    # Bia
    elif "rmdir" in read: # verificar se ponteiros iNode esta vazia e olhar o pai
        print(f'Diretório {nome[1]} removido')
    
    # Ryan
    elif "ls" in read:  # listar os nome dos ponteiros iNodes
        print(f'Conteúdo do diretório {nome[1]}:')
    
    # Ryan
    elif "cd" in read:  # mover para o bloco do iNode selecionado da lista de iNodes (. permanece no mesmo diretorio, .. move um diretorio para tras)
        print(f'Diretório {nome[1]} selecionado')
            
    # Bia
    elif "kill" in read: # encerra o programa           
        print("Programa encerrado")
        return "kill"
    
    else:
        print("Comando não reconhecido")
    