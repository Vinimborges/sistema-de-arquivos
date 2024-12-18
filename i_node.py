class Inode:
   def __init__(self, nome, criador, data_criacao):
       self.nome = nome
       self.criador = criador
       self.dono = criador
       self.tam = '0'
       self.data_de_criacao = data_criacao
       self.data_de_modificacao = data_criacao
       self.permissoes = 'oi'                #leitura/escrita/execucao
    #    self.ponteiros_blocos = None
    #    self.ponteiros_iNodes = None
       self.ponteiros_blocos = []
       self.ponteiros_iNodes = []
