
a = True
b = False

# Operadores lógicos -> and

c = a and b

print('a e b são iguais?',c)

# Operadores lógicos -> or

d = a or b
e = a | b

print('A e B são iguais?', d, e)

# Operadores lógicos -> not

f = not a
g = not b

print('\nA negado:', f, '\nB negado:', g)

# Operadores relacionais

h = 4 > 2

# Exercícios

especiesA = int(input('Qual o número de espécies coletadas na seção A?'))
individuosA = int(input('Qual o número de indivíduos coletados na seção A?'))

mediaA = individuosA / especiesA

especiesB = int(input('Qual o número de espécies coletadas na seção B?'))
individuosB = int(input('Qual o número de indivíduos coletados na seção B?'))

mediaB = individuosB / especiesB

maiorOuIgual = individuosA >= individuosB
diferente = individuosA != individuosB
ou = individuosA > individuosB or mediaA > mediaB
diferenca = individuosA != individuosB and mediaA != mediaB

print('O maior ou igual', maiorOuIgual)
print('Diferente', diferente)
print(mediaA, '\n', mediaB)
print('Operador or', ou)
print('Diferença', diferenca)