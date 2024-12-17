
# Sistema de Arquivos 

Este trabalho tem como objetivo desenvolver um sistema de arquivos baseado em i-nodes.
## Features

### Operações sobre arquivos:
- Criar arquivo (touch arquivo)
- Remover arquivo (rm arquivo)
- Criar um arquivo já adicionando conteúdo (echo "conteúdo legal" > arquivo)
- Adicionar conteúdo a um arquivo existente ou criá-lo caso não exista (echo "conteudo legal" >> arquivo)
- Ler arquivo (cat arquivo)
- Copiar arquivo (cp arquivo1 arquivo2)
- Renomear/mover arquivo (mv arquivo1 arquivo2)
- Criar links entre arquivos (ln -s arquivoOriginal link)

### Operações sobre diretórios:
-  Criar diretório (mkdir diretorio)
- Remover diretório (rmdir diretorio)
- Listar o conteúdo de um diretório (ls diretório)
- Trocar de diretório (cd diretorio)
- Renomear/mover diretório (mv diretorio1 diretorio2)
- Criar links entre diretório (ln -s arquivoOriginal link)

## Installation

Siga os passos abaixo para garantir que o código seja executado corretamente:

### 1. Instalar Dependências
Certifique-se de que o Python esteja instalado. Em seguida, execute o seguinte comando para instalar a biblioteca necessária:
```bash
  pip install colorama
```

### 2. Gerar Arquivo Necessário
Após instalar as dependências, rode o script responsável por gerar o arquivo necessário para a execução do programa principal:
```bash
  python ./gerar_arquivo.py
```

### 3. Executar o Programa Principal
Por fim, execute o programa principal utilizando o comando:
```bash
  python ./main.py
```
    
## Authors

- [@Beatriz-SMB](https://github.com/Beatriz-SMB)
- [@Knoshz](https://github.com/Knoshz)
- [@RyanBLeon28](https://github.com/RyanBLeon28)
- [@Vinimborges](https://github.com/Vinimborges)

