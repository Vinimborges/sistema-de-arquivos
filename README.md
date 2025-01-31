
# Segurança no sistema de arquivos 

Este projeto implementa mecanismos de segurança em um sistema de arquivos, permitindo o gerenciamento de múltiplos usuários, cada um com sua própria área de armazenamento (home do usuário). Todos os arquivos e diretórios possuem um usuário proprietário associado, bem como permissões de acesso que definem se operações de leitura e escrita podem ser realizadas.
## Features

- Gerenciamento de múltiplos usuários com senhas seguras.
- Definição de permissões de leitura e escrita para arquivos e diretórios.
- Comandos chmod para alteração de permissões.
- Comando chown para modificação do dono do arquivo ou diretório.
- Armazenamento seguro de senhas, sem uso de texto plano.
- Proteção do arquivo de senhas contra acesso não autorizado.

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

