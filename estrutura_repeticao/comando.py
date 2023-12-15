
for numero in range(0, 5):
    print(numero)

for num in range(5, 0, 2): # o for em python, permite que você coloque na condição de quanto em quanto valor você quer que ele imprima. Isso é terceiro valor
    print('\n', num)

soma = 0

for numero in range(1, 6):
    soma = soma + numero
    print('Aqui o soma', soma)

palavra = 'sorvete'

for letra in palavra: # aqui o for vai percorrer a variável palavra
    if letra == 'v':
        print('Achamos a letra ', letra)
