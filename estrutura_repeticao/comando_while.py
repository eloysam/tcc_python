# Exemplo 1
print('Exemplo 1')

"""
casa = 'casamento'

while casa != 'casamento':
    if 
"""

numero = 1
while numero < 6:
    print(numero)
    numero += 1
print('---')

print('Exemplo 2')
numero = 5
while numero > 0:
    print(numero)
    numero -= 1

print('Exemplo 3')

normal = 1 + 2 +3 + 4 + 5
soma = 0
nuumero = 1

while numero < 6:
    soma = soma + numero
    numero += 1
print('Dentro do while:',soma)
print('Fora do while:',normal)

numero = 17
while numero < 1 or numero > 10: # é últil para validação
    numero = int(input('Digite um número de 1 a 10:'))