from criptografia import criptografar
from i_node import Inode
from datetime import date

def cadastrar_usuario(lista_inodes,lista_users):
    data_criacao = date.today() # Pega a data em que o arquivo foi criado
    data_criacao_formatada = data_criacao.strftime('%d/%m/%Y')
    nome = input("Digite o nome de usuário que deseja cadastrar: ")
    senha = input("Digite uma senha de no mínimo 8 dígitos (Apenas letras): ")
    if len(senha) < 8:
        print("Tamanho mínimo de senha não respeitado")
    else:
        print(f'Usuário {nome} cadastrado com sucesso')
        lista_users.append(dict(user=nome, password=criptografar(senha)))
        lista_inodes.append(Inode(lista_inodes[len(lista_inodes)-1].id + 1,nome,nome,data_criacao_formatada))
    return lista_inodes,lista_users