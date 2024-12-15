from manipulacaoArquivos import controle_inodes
from manipulacaoArquivos import ler_memoria

mem = ler_memoria.Ler_memoria() # Lê toda a memória
lista_inodes = controle_inodes.Controle_inodes(mem) # Cria uma lista com os Inodes

def ls(entrada,diretorioPai,diretorioAtual):
    if len(entrada) > 1:
        print(f'Too much arguments')
        return diretorioAtual
    print(f'Conteúdo do diretório:')
    for iNode in lista_inodes:  
        if diretorioPai == iNode.nome:
            for  filhos in iNode.ponteiros_iNodes:
                print(filhos.nome)
    return diretorioAtual
    