def escrever_em_bloco(nome_disco, numero_bloco, conteudo, tamanho_bloco):
    with open(nome_disco, "r+") as disco:
        posicao = numero_bloco * tamanho_bloco
        disco.seek(posicao)
        conteudo_binario = conteudo[:tamanho_bloco]
        conteudo_binario += "0" * (tamanho_bloco - len(conteudo_binario))  # Preenche com zeros
        conteudo_binario += "\n"
        disco.write(conteudo_binario)

# Escrever "Olá Mundo" no bloco 0
escrever_em_bloco("disco.txt", 0, "SuperBlock|", 4096)