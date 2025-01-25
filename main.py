'''
    Estrutura da memoria
    [GerInodes, GerBlock, Blocks]
'''
from cadastrar_usuario import cadastrar_usuario
from login import login

from manipulacaoArquivos.ler_memoria import Ler_memoria
from manipulacaoArquivos.controle_blocos import Controle_blocos
from manipulacaoArquivos.controle_inodes import Controle_inodes
from manipulacaoArquivos.blocos import Blocos
from manipulacaoArquivos.users import Users

from colorama import Fore, Back, Style, init
# Initialize Colorama
init(autoreset=True)

from comandos.entrada import tratar_entrada

mem = Ler_memoria() # Lê toda a memória

lista_inodes = Controle_inodes(mem) # Cria uma lista com os Inodes
lista_controle_blocos = Controle_blocos(mem) # Cria uma lista de blocos livres e ocupados
lista_blocos = Blocos(mem) # Cria uma lista com o conteúdo armazenado nos blocos
lista_users = Users(mem)

espaco_livre = 0

for i in range(len(lista_controle_blocos)-1): # Verifica quanto espaço livre tem
    if lista_controle_blocos[i] == "0":
        espaco_livre += 4


print(f'Espaço livre para armazenamento: {espaco_livre//1028} MB')

diretorioAtual = 'home'

if __name__ == "__main__":
    while(True):
        op = int(input("Digite 1 para cadastrar usuário ou 2 para logar: "))
        if op == 1:
            cadastrar_usuario(lista_inodes,lista_users)
        elif op == 2:
            diretorioAtual = diretorioAtual + '/' + login(lista_users)
            while(True):    
                print(diretorioAtual)
                print('~',Fore.GREEN +'$'+Style.RESET_ALL+'/'+diretorioAtual,end="/ ")
                comando = input()
                retorno = tratar_entrada(diretorioAtual,comando,mem,lista_inodes,lista_controle_blocos,lista_blocos,lista_users)
                if retorno == "kill":

                    #pegar toda as novas informcoes da lista Inode, Blocos e controle dos blocs e escrever na memoria
                    break
                else:
                    diretorioAtual = retorno  #atualiza o estado do diretorio atual
            break
        else: 
            print("Opção inválida")    
        # print(f'Você digitou {comando}')
        



# Lista de comandos para implentar (Dar um Ok para os que estiverem concluidos)

# Operações sobre arquivos:
#     - Criar arquivo (touch arquivo)
#     - Remover arquivo (rm arquivo)
#     - Criar um arquivo já adicionando conteúdo (echo "conteúdo legal" > arquivo)
#     - Adicionar conteúdo a um arquivo existente ou criá-lo caso não exista (echo "conteudo legal" >> arquivo)
#     - Ler arquivo (cat arquivo)
#     - Copiar arquivo (cp arquivo1 arquivo2)
#     - Renomear/mover arquivo (mv arquivo1 arquivo2)
#     - Criar links entre arquivos (ln -s arquivoOriginal link)

# Operações sobre diretórios:
#     - Criar diretório (mkdir diretorio)
#     - Remover diretório (rmdir diretorio) - só funciona se diretório estiver vazio
#     - Listar o conteúdo de um diretório (ls diretório)
#     - Trocar de diretório (cd diretorio)
#         * Não esquecer dos arquivos especiais . e .. 
#     - Renomear/mover diretório (mv diretorio1 diretorio2)
#     - Criar links entre diretório (ln -s arquivoOriginal link)