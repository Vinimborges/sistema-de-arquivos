from i_node import Inode
from ler_memoria import Ler_memoria

mem = Ler_memoria()

lista_inodes = []
espaco_livre = 0
index_inicio_inodes = 10000000
for i, mem in enumerate(mem):
    if "Inodes" in mem or (mem[0] != '\x00' and i > 0): # Função que busca os Inodes que estão salvos na memória
        if "Inodes" in mem:
            index_inicio_inodes = i
        temp = mem.split("|")
        print(temp)
        temp.pop(0)
        for i, temp in enumerate(temp):
            temp1 = temp.split(",")
            nome = temp1.pop(0)
            criador = temp1.pop(0)
            inode = Inode(nome, criador)
            inode.dono = temp1.pop(0)
            inode.tam = temp1.pop(0)
            inode.data_de_criacao = temp1.pop(0)
            inode.data_de_modificacao = temp1.pop(0)
            inode.permissoes = temp1.pop(0)
            inode.ponteiros_blocos = temp1.pop(0)
            if "\x00" in temp1[0]:
                tirar_zeros = temp1[0].split("\x00")
                print(tirar_zeros[0])
                inode.ponteiros_iNodes = tirar_zeros.pop(0)
            print(tirar_zeros)
            lista_inodes.append(inode)
            print(lista_inodes[0].criador)
            print(lista_inodes[0].dono)
            print(lista_inodes[0].ponteiros_iNodes)
    elif i > index_inicio_inodes and mem[0] == "\x00":
        espaco_livre += 4

print(f'Espaço livre para armazenamento: {espaco_livre//1028} MB')
        

def criar_arquivo(nome):
    lista_inodes.append(Inode(nome, "eu"))
    print(f'Nome do arquivo criado: {lista_inodes[len(lista_inodes)-1].nome}')
    for pos in enumerate(lista_inodes):
        print(pos[1].nome)
    
while(True):
    read = input()
    print(f'Você digitou {read}')
    
    if "touch" in read: # Cria arquivo
        nome = read.split()
        criar_arquivo(nome[1])
    
    elif "rm" in read: # Remove arquivo
        nome = read.split()
        print(f'Nome do arquivo excluído: {nome[1]}')
        # remove_arquivo(nome[1])
    elif "echo" in read: 
        nome = read.split(">")
        print(nome)
        print(type(nome))
        if len(nome) == 2: #Cria um arquivo já adicionando conteúdo 
            print("um")
        elif len(nome) == 3: #Adiciona conteúdo a um arquivo existente ou cria caso não exista
            print("dois")
    elif "cat" in read: # Lê o arquivo
        nome = read.split()
        print(f'Lendo o arquivo: {nome[1]}')
        # criar_arquivo(nome[1])
    elif "cp" in read: #Copia arquivo
        nome = read.split()
        print(f'Copiando o arquivo {nome[1]} para o arquivo {nome[2]}')
    elif "mv" in read: #Move/Renomeia arquivo
        nome = read.split()
        if "/" in nome[2]:
            sep = nome[2].split("/")
            print(f'Movendo o arquivo {nome[1]} para o diretório {sep[0]} com o nome {sep[1]}')
        else:
            print(f'Renomeando o arquivo {nome[1]} para {nome[2]}')
    elif "ln" in read:
        nome = read.split()
        print(f'Criado o link {nome[3]} para o arquivo {nome[2]}')
        
    elif "mkdir" in read: #Cria um diretório
        nome = read.split()
        print(f'Nome do diretório criado: {nome[1]}')
        
    elif "rmdir" in read:
        nome = read.split()
        print(f'Diretório {nome[1]} removido')
    
    elif "ls" in read:
        nome = read.split()
        print(f'Conteúdo do diretório {nome[1]}:')
    
    elif "cd" in read:
        nome = read.split()
        print(f'Diretório {nome[1]} selecionado')
            
            
    elif "kill" in read: # encerra o programa
        print("Programa encerrado")
        break

    else:
        print("Comando não reconhecido")