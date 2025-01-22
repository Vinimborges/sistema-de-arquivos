class Inode:
   def __init__(self,id_inode, nome, criador, data_criacao):
       self.id = id_inode
       self.nome = nome
       self.criador = criador
       self.dono = criador
       self.tam = '0'
       self.data_de_criacao = data_criacao
       self.data_de_modificacao = data_criacao
       self.permissoes_dono = "r+w+e"                #leitura/escrita/execucao
       self.permissoes_outros = "r+w+e"
    #    self.ponteiros_blocos = None
    #    self.ponteiros_iNodes = None
       self.ponteiros_blocos = []
       self.ponteiros_iNodes = []
