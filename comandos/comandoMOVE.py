
def mv(diretorioAtual, diretorioPai, lista_inodes, lista_blocos, entrada):
    print(f'Diretorio: {diretorioAtual}')
    diretorioAtualSeparado = diretorioAtual.split()

    if(entrada[0] in diretorioPai.ponteiros_inodes and entrada[1] in diretorioPai.ponteiros_inodes):
        print('os iNodes estao nesse diretorio')
        
    else:
        print('Um dos iNodes nao esta nesse diretorio')

    return diretorioAtual

def mv_Renomear(diretorioAtual):
    return diretorioAtual