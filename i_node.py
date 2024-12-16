class Inode:
   def __init__(self, nome, criador):
       self.nome = nome
       self.criador = criador
       self.dono = criador
       self.tam = 'oi'
       self.data_de_criacao = 'oi'
       self.data_de_modificacao = 'oi'
       self.permissoes = 'oi'                #leitura/escrita/execucao
    #    self.ponteiros_blocos = None
    #    self.ponteiros_iNodes = None
       self.ponteiros_blocos = []
       self.ponteiros_iNodes = []
