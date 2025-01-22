def criptografar(texto):
  """Cifra de César simples.

  Args:
    texto: Texto a ser cifrado.
    deslocamento: Número de posições a serem deslocadas no alfabeto.

  Returns:
    Texto cifrado.
  """

  texto_cifrado = ""
  for letra in texto:
    if letra.isalpha():
      # Verifica se é maiúscula ou minúscula e ajusta o deslocamento
      if letra.isupper():
        novo_indice = (ord(letra) - ord('A') + 3) % 26
        novo_caractere = chr(novo_indice + ord('A'))
      else:
        novo_indice = (ord(letra) - ord('a') + 3) % 26
        novo_caractere = chr(novo_indice + ord('a'))
      texto_cifrado += novo_caractere
    else:
      # Se não for letra, mantém o caractere original
      texto_cifrado += letra
  return texto_cifrado

def descriptografar(texto):

  texto_cifrado = ""
  for letra in texto:
    if letra.isalpha():
      # Verifica se é maiúscula ou minúscula e ajusta o deslocamento
      if letra.isupper():
        novo_indice = (ord(letra) - ord('A') - 3) % 26
        novo_caractere = chr(novo_indice + ord('A'))
      else:
        novo_indice = (ord(letra) - ord('a') - 3) % 26
        novo_caractere = chr(novo_indice + ord('a'))
      texto_cifrado += novo_caractere
    else:
      # Se não for letra, mantém o caractere original
      texto_cifrado += letra
  return texto_cifrado

