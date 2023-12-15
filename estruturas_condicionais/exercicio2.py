    # ANALISANDO PARÂMETROS HEMATOLÓGICOS

hemacias = float(input('Digite o valor das hemácias (x10^12/L):'))
hemoglobina = float(input('Digite o valor da hemoglobina (g/dL):'))
hematocrito = float(input('Digite o valor do hematócrito (%):'))

if hemacias > 4.5 and hemacias < 5.5:
    print('As hemácias estão normais!')
else:
    if hemacias < 4.5:
        print('As hemácias estão baixas!')
    elif hemacias > 5.5:
        print('As hemácias estão altas!')

if hemoglobina > 13 and hemoglobina < 17:
    print('As hemoglobinas estão normais!')
else:
    if hemoglobina < 13:
        print('As hemoglobinas estão baixas!')
    elif hemoglobina > 17:
        print('As hemoglobinas estão altas!')

if hematocrito > 40 and hematocrito < 50:
    print('Os hematócritos estão normais!')
else:
    if hematocrito < 40:
        print('Os hematócritos estão baixos!')
    elif hematocrito > 50:
        print('Os hematócritos estão altos!')


