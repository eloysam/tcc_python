# ******************** Exercício 02 ****************************************************
# Vamos analizar sequência de proteín(as proteínas podem ser representadas por letra, onde cada aminoácido é uma letra)
# a) Quanto (%) a proteína mutante é maior que a normal
# b) O comprimento de aa's de cada proteína
# c) A porcentagem de serina (S) nas duas sequências (count)

print('\n\n\tEXERCICIO 02')
proteina = 'MGTAHDBSJVFMSBDBFKSLDB'
proteinaMutante = 'DNFKJSJBFJSBVNRUGHGDKLSNFUOZN'

# letra A
if len(proteinaMutante) > len(proteina):
    valor = float((len(proteinaMutante) - len(proteina)))/100
    print('A proteína mutante é maior:',valor,'%')
else:
    print('Tente novamente! Obrigada')


# letra B
print(len(proteina))
print(len(proteinaMutante))

# letra C

