price = float(input('Qual é o valor do produto?'))
print(f'Valor do produto em {price} reais...Analisando dados...')
answer = str(input('Deseja aplicar 5 porcento de desconto no valor do produto?'))

valort = price * 5
valorb = valort / 100

if answer == 'Sim':
    print(f'Pois bem... O desconto é de {valorb} reais.')
else:
    print(f'Muito obrigado pela compra! O valor ficará em {price} reais.')