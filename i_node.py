class Inode:
   def __init__(self, nome, criador):
       self.nome = nome
       self.criador = criador
       self.dono = criador
       self.tam = None
       self.data_de_criacao = None
       self.data_de_modificacao = None
       self.permissoes = None
       self.ponteiros_blocos = None
       self.ponteiros_iNodes = None
