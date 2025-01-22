from criptografia import criptografar
def cadastrar_usuario():
    nome = input("Digite o nome de usuário que deseja cadastrar: ")
    senha = input("Digite uma senha de no mínimo 8 dígitos (Apenas letras): ")
    with open("usuarios.txt", "a") as usuarios_db:
        linha = "\n" + nome + " " + criptografar(senha)
        usuarios_db.write(linha)
    