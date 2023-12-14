# No python existe um conceito de identação

if 5 > 9:
    print('5 é maior que 3')
print('teste') # aqui está fora do IF

if 5 > 6:
    print('5 é maior')
else:
    print('6 é maior')

n = int(input('Digite um valor:'))

if n % 2 == 0:
    print(n, 'é par!')
else:
    if n % 3 == 0:
        print(n, 'é divisível por 3')
    else:
        print('Tente outra vez!')