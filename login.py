from criptografia import descriptografar

usuarios = []

        
with open("usuarios.txt", "r+") as usuarios_db:
    conteudo_usuarios = usuarios_db.readlines()
    lista_usuarios = list(conteudo_usuarios)
    for i in range(len(lista_usuarios)):
        sep = lista_usuarios[i].rstrip().split()
        infos_usuario = dict(user=sep[0], password=descriptografar(sep[1]))
        usuarios.append(infos_usuario)
        print(infos_usuario["password"])
    print(usuarios)
    
def login():
    while(True):
        user = input("Digite o nome de usuário: ")
        for posicao in usuarios:
            if posicao["user"] == user:
                password = input("Digite a senha: ")
                if posicao["password"] == password:
                    print("Login permitido")
                    return user
                else:
                    print("Senha inválida")
        print("Usuário inválido")
