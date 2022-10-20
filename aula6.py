user = 'Dennis Pilgrim'

score1 = float(input(f'A nota do aluno {user} da primeira prova é:'))
score2 = float(input(f'A note do aluno {user} da segunda prova é:'))

calc = score1 + score2
scoreabsolute =  calc / 2

print(f'A média aritimética das notas acima é de {scoreabsolute}')