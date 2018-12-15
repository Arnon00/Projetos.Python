import random

non = []
sort = random.randint(0, 3)

for i in range(0, 4):
    non.append(str(input('Digite o nome dob {} aluno: '.format(i+1))))
else:
    print('Voce Cadastrou: {} alunos'.format(len(non)))



print('\n O aluno escolhido foi: {}'.format(non[sort]))
