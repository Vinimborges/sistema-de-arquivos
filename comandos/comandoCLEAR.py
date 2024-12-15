import os

def clear(diretorioAtual):
    if os.name == 'nt': #windows
        os.system('cls')
    else:               # Linux/Mac
        os.system('clear')
    return diretorioAtual
    
