from criptografia import descriptografar

usuarios = []
 
    
def login(lista_users):
    # with open("usuarios.txt", "r+") as usuarios_db:
    #     conteudo_usuarios = usuarios_db.readlines()
    usuarios = lista_users
    print(len(usuarios))
    # for i in range(len(lista_usuarios)):
    #     sep = lista_usuarios[i].rstrip().split()
    #     infos_usuario = dict(user=sep[0], password=descriptografar(sep[1]))
    #     usuarios.append(infos_usuario)
    #     print(infos_usuario["password"])
    print(usuarios)
    while(True):
        user = input("Digite o nome de usuário: ")
        for posicao in usuarios:
            if posicao["user"] == user:
                password = input("Digite a senha: ")
                if descriptografar(posicao["password"]) == password:
                    print("Login permitido")
                    return user
                else:
                    print("Senha inválida")
            elif posicao == len(usuarios)-1 and posicao["user"] != user:     
                print("Usuário inválido")
