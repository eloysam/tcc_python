
# Transcrição de sequência de DNA

dna = str(input('Escreva uma sequência de DNA:')).upper()

rna = ''
for nucleotideo in dna:
    if nucleotideo == 'A':
        rna = rna + 'U'
    elif nucleotideo == 'T':
        rna = rna + 'A'
    elif nucleotideo == 'C':
        rna = rna + 'G'
    elif nucleotideo == 'G':
        rna = rna + 'C'

print(f'A sequência de RNA correspondente ao DNA é: {rna}')
