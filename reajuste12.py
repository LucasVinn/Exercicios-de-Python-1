wage = float(input('Quanto é seu salário atual nesta empresa?'))

grow = wage * 15
calc = wage / 100
calo = calc + wage

answer = str(input('Você deseja ter um aumento salarial de 15 porcento?'))

if answer == 'Sim':
    print(f'O reajuste salarial é de {calo}')
else:
    print(f'Então seu salário continua em {wage}')
