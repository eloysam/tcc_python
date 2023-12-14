# No python existe um conceito de identação

if 5 > 9:
    print('5 é maior que 3')
print('teste') # aqui está fora do IF

if 5 > 6:
    print('5 é maior')
else:
    print('6 é maior')

n = 3

if n == 4:
    print('n = 4')
else:
    if n == 3:
        print('n é igual a 3')
    else:
        print('n != 3 && n!= 4')