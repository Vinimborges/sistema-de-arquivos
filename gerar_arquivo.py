
def criar_disco(nome_disco, tamanho_mb):
    qtd_blocos = (tamanho_mb * 1024 * 1024) /(4*1024) 
    with open(nome_disco, "w") as disco:
        while qtd_blocos > 0:
            disco.write(f'\0' * (4 * 1024 - 2))  # Preenche com bytes nulos
            disco.write(f'\n')
            qtd_blocos -= 1
            
# Criar um "disco" de 256 MB
criar_disco("disco.txt", 256)
