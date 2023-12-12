# ******************** Exercício 02 ****************************************************
# Vamos analizar sequência de proteín(as proteínas podem ser representadas por letra, onde cada aminoácido é uma letra)
# a) Quanto (%) a proteína mutante é maior que a normal
# b) O comprimento de aa's de cada proteína
# c) A porcentagem de serina (S) nas duas sequências (count)

print('\n\n\tEXERCICIO 02')
proteina = 'MGTAHDBSJVFMSBDBFKSLDB'
proteinaMutante = 'DNFKJSJBFJSBVNRUGHGDKLSNFUOZN'

# letra A

tam1 = len(proteina)
tam2 = len(proteinaMutante)

razao = ((tam2/tam1)- 1)*100
print('O comprimento da proteina 1 é de:', len(proteina), 'aas')
print('O comprimento da proteina 2 é de:', len(proteinaMutante), 'aas')




"""
if len(proteinaMutante) > len(proteina):
    valor = float((len(proteinaMutante) - len(proteina)))/100
    print('A proteína mutante é maior:',valor,'%')
else:
    print('Tente novamente! Obrigada')

"""


