a = 'casaco'

# Funções do python
maiuscula = a.upper()
minuscula = a.lower()
capital = a.capitalize()

# podemos escolhelher qual parte da palavra queremos
metadePalavra = a[5:6] # você escolhe as partes da palavra que você deseja
ultimasLetras = a[3:] # Pega as últimas letras na frase a partir da posição que você inserir

print(a,'\n', maiuscula,'\n', minuscula,'\n', capital, '\n', metadePalavra, '\n', ultimasLetras)

# Função REPLACE
b = a.replace('aco', 'inha') # Aqui você substitui algum valor que você quer
c = a.replace('o', 'a')
print(a)
print(b)

# Função FIND
print(c.find('s')) # com a função FIND você encontra em que posição está a letra 's'
print(c.find('t'))

e = ' casaco '
print(len(e)) # a função 'len' retorna o comprimento da string

f = a.strip() # essa função tira todos os espaços
print(len(f))

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2}: o resultado é {n1/n2}') # o f significa formatação, significa que você quer entregar algo formatado