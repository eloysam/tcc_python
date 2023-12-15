# IDENTIFICANDO FAMÍLIAS TAXONÔMICAS

nome_plantas = str(input('Digite o nome de uma família de plantas:'))
nome_animais = str(input('Digite o nome de uma família de animais:'))

# poderíamos usar o comando IN 
ini = nome_plantas.find('ace')
fim = nome_plantas.find(' ')
P_nome = nome_plantas[ini:fim]
ini2 = nome_animais.find('ida')
fim2 = nome_plantas.find(' ')
A_nome = nome_animais[ini2:fim2]

# else if == elif
if nome_plantas[ini:fim] == 'acea':
    print(nome_plantas, 'pertence á Família de plantas!')
elif nome_animais[ini2:fim2]:
    print(nome_animais, 'pertence á Família dos animais!')
else:
    print('Táxon não-identificado')

