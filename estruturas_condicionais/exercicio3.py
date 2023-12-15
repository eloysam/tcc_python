 # DETECTANDO CÓDONS DE INICIAÇÃO E TERMINAÇÃO

RNA = str(input('Digite uma sequência de RNA:'))

rna = RNA.upper()

if 'AUG' in rna:
    if ('UGA' or 'UAA' or 'UAG') in rna:
        print('A sequência possui códon de iniciação e códon de terminação!')
    else:
        print('A sequência possui somente apenas códon de iniciação!')
else:
    if ('UGA' or 'UAA' or 'UAG') in rna: # Isso não está funcionando!
        print('A sequência possui apenas códon de terminação!')
    else:
        print('A sequência não possui códon algum!')


