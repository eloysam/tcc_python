
print('\tEXERCÍCIO 01')

nome = str(input('Insira o nome da espécie:'))
capitalize = nome.capitalize()

comeco = capitalize.find(capitalize[1]) # aqui eu estou pegando a segunda letra
fim = capitalize.find(' ') # aqui eu estou pegando a parte que termina a palavra, ou seja até o espaço com a outra palavra
substituicao = capitalize[comeco:fim]
abreviacao = capitalize.replace(substituicao,'.')
print('O nome', nome,'abreveado é', abreviacao)

