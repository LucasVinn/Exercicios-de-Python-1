a = input('Digite algo:')

print(a)

print(f'O tipo primitivo é {type(a)}')
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
