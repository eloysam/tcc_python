    # ANALISANDO PARÂMETROS HEMATOLÓGICOS

hemacias = float(input('Digite o valor das hemácias:'))
hemoglobina = float(input('Digite o valor da hemoglobina:'))
hematocrito = float(input('Digite o valor do hematócrito:'))

if hemacias > 4.5 and hemacias < 5.5:
    print('As hemácias estão normais!')
else:
    if hemacias < 4.5:
        print('As hemácias estão baixas!')
    if hemacias > 5.5:
        print('As hemácias estão altas!')

if hemoglobina > 13 and hemoglobina < 17:
    print('As hemoglobinas estão normais!')
else:
    if hemoglobina < 13:
        print('As hemoglobinas estão baixas!')
    if hemoglobina > 17:
        print('As hemoglobinas estão altas!')

if hematocrito > 40 and hematocrito < 50:
    print('Os hematócritos estão normais!')
else:
    if hematocrito < 40:
        print('Os hematócritos estão baixos!')
    if hematocrito > 50:
        print('Os hematócritos estão altos!')


