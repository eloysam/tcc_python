
print('\nExemplo 0')
for numero in range(0, 5):
    print(numero)

# Exemplo 1
print('\nExemplo 1')
for num in range(5, 0, 2): # o for em python, permite que você coloque na condição de quanto em quanto valor você quer que ele imprima. Isso é terceiro valor
    print('\n', num)

soma = 0

for numero in range(1, 6):
    soma = soma + numero
    print('Aqui o soma', soma)

# Exemplo 2
print('\nExemplo 2')
palavra = 'sorvete'
for letra in palavra: # aqui o for vai percorrer a variável palavra | parece o foreach
    if letra == 'v':
        print('Achamos a letra ', letra)

# Exemplo 3
print('\nExemplo 3')
soma = 0
for numero in range(1, 7):
    soma = soma + numero
   # print('A soma se deu por:', soma)

print('Aqui pega o total:', soma)

# Exemplo 4
print('\nExemplo 4')
for i in range(0, 5):
    print(i)
    print('---')
    for j in range(0,3):
        print(j)
    print()
