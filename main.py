'''
    Estrutura da memoria
    [GerInodes, GerBlock, Blocks]
'''
from cadastrar_usuario import cadastrar_usuario
from login import login

from colorama import Fore, Back, Style, init
# Initialize Colorama
init(autoreset=True)

from comandos.entrada import tratar_entrada

diretorioAtual = 'home'

if __name__ == "__main__":
    while(True):
        op = int(input("Digite 1 para cadastrar usuário ou 2 para logar: "))
        if op == 1:
            cadastrar_usuario()
        elif op == 2:
            diretorioAtual = diretorioAtual + '/' + login()
            print(diretorioAtual)
            print('~',Fore.GREEN +'$'+Style.RESET_ALL+'/'+diretorioAtual,end="/ ")
            comando = input()
            retorno = tratar_entrada(diretorioAtual,comando)
            if retorno == "kill":

                #pegar toda as novas informcoes da lista Inode, Blocos e controle dos blocs e escrever na memoria
                break
            else:
                diretorioAtual = retorno  #atualiza o estado do diretorio atual
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