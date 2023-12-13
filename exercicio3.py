"""
    A sequência abaixo representa um pré-mRNA não processado, no qual os íntrons não foram removidos. Essa sequência possui um éxon, que começa com AUG e termina com um stop códon UAG (esse códon não extraído como proteína). Determine em que posições começam os códons de iniciação e parada e retorne o éxon dessa sequência
"""

seqRNA = 'AAAUUUAUGUUCCCUUUGGGUGGGCCCGGGAAAUAGGUUCUUGUUUAAAUUC'

# Posições dos códons de iniciação e terminação
comeco = seqRNA.find('AUG')
fim = seqRNA.find('UAG')
exon = seqRNA[comeco:fim]
print('A região coficadora é:', exon)
